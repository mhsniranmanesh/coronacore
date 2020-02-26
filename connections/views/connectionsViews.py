from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from connections.models.connections import Contact
from connections.serializers.connectionsSerializers import ConnectionsAddContactSerializer


class ConnectionsAddContact(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = ConnectionsAddContactSerializer(data=request.data, many=True)
        if serializer.is_valid():
            try:
                user = request.user
                if len(serializer.validated_data) > 100 :
                    return Response(data={'message': 'maximum acceptable batch size is 100'},
                                    status=status.HTTP_400_BAD_REQUEST)
                for contact in serializer.validated_data:
                    print(contact.keys())
                    if 'name' in contact.keys() and 'phone_number' in contact.keys():
                        name = contact['name']
                        phone_number = contact['phone_number']
                        contact_obj = Contact(name=name, phone_number=phone_number, user=user)
                        contact_obj.save()

                return Response(data={'message': 'success'},status=status.HTTP_200_OK)

            except Exception as e:
                return Response(data={'message': 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
