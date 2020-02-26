from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from profiles.models.user import User
from profiles.serializers.userSerializers import CreateUserSerializer, UserUpdateInfosSerializer
from profiles.utils.userUtils import create_user_random_password


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    lookup_field = 'phone_number'

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User(
                    username=serializer.validated_data['phone_number'],
                    name=serializer.validated_data['name'],
                    phone_number=serializer.validated_data['phone_number'],
                )
                password = create_user_random_password()
                user.set_password(password)
                user.save()
                return Response(
                    data={'phone_number': user.phone_number,
                          'name': user.name,
                          'username': user.username,
                          'password': user.password
                          },
                    status=status.HTTP_200_OK
                )
            except IntegrityError:
                return Response(data={'phone_number': ['User with this phone number already exists']},
                                status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print(e)
                return Response(data={'message': 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateInfosView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = UserUpdateInfosSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = request.user
                if 'name' in serializer.validated_data.keys():
                    user.name = serializer.validated_data.get('name')
                if 'age' in serializer.validated_data.keys():
                    user.age = serializer.validated_data.get('age')
                if 'status_code' in serializer.validated_data.keys():
                    user.status_code = serializer.validated_data.get('status_code')
                if 'gender' in serializer.validated_data.keys():
                    user.gender = serializer.validated_data.get('gender')
                user.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response(data={'message': 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





