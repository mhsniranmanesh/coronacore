from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from connections.constants.connectionConstants import MAX_CONTACT_NUMBERS_IN_REQUEST, MAX_CONNECTION_REQUEST__NUMBERS
from connections.models.connections import Contact, ConnectionRequest, Connection
from connections.serializers.connectionsSerializers import ConnectionsAddContactSerializer, \
    ConnectionsRequestConnectionSerializer, GetUserConnectionRequestsSerializer, ConnectionsAcceptConnectionSerializer
from profiles.models.user import User


class ConnectionsAddContact(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = ConnectionsAddContactSerializer(data=request.data, many=True)
        if serializer.is_valid():
            try:
                user = request.user
                if len(serializer.validated_data) > MAX_CONTACT_NUMBERS_IN_REQUEST :
                    return Response(data={'message': 'maximum acceptable batch size exceeded'},
                                    status=status.HTTP_400_BAD_REQUEST)
                for contact in serializer.validated_data:
                    if 'name' in contact.keys() and 'phone_number' in contact.keys():
                        name = contact['name']
                        phone_number = contact['phone_number']
                        contact_obj = Contact(name=name, phone_number=phone_number, user=user)
                        contact_obj.save()

                return Response(data={'message': 'success'}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response(data={'message': 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConnectionsRequestConnection(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = ConnectionsRequestConnectionSerializer(data=request.data, many=True)

        if serializer.is_valid():
            try:
                user = request.user
                if len(serializer.validated_data) > MAX_CONNECTION_REQUEST__NUMBERS :
                    return Response(data={'message': 'maximum acceptable batch size exceeded'},
                                    status=status.HTTP_400_BAD_REQUEST)
                for connection in serializer.validated_data:
                    if 'phone_number' in connection.keys() and 'type' in connection.keys():
                        type = connection['type']
                        phone_number = connection['phone_number']
                        if phone_number == user.phone_number:
                            continue
                        connection_request = ConnectionRequest(user=user, phone_number=phone_number, type=type)
                        connection_request.save()

                return Response(data={'message': 'success'}, status=status.HTTP_200_OK)

            except Exception as e:
                print(e)
                return Response(data={'message': 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConnectionsAcceptConnection(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = ConnectionsAcceptConnectionSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = request.user
                accepted_user_uuid = serializer.validated_data['uuid']
                accepted_user = User.objects.get(uuid=accepted_user_uuid)
                user_request = ConnectionRequest.objects.filter(phone_number=accepted_user.phone_number).latest('id')
                accepted_user_request = ConnectionRequest.objects.filter(phone_number=user.phone_number).latest('id')
                user_connection = Connection(self_user=user, other_user=accepted_user, type=user_request.type)
                accepted_user_connection = Connection(self_user=accepted_user, other_user=user,
                                                      type=accepted_user_request.type)
                user_connection.save()
                accepted_user_connection.save()
                return Response(data={'message': 'success'}, status=status.HTTP_200_OK)
            except ConnectionRequest.DoesNotExist:
                return Response(data={'message': 'connection request does not exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                return Response(data={'message': 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserConnectionRequests(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        try :
            requests = ConnectionRequest.objects.filter(phone_number=user.phone_number)
            serializer = GetUserConnectionRequestsSerializer(requests, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'message': 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
