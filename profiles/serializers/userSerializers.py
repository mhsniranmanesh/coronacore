from rest_framework import serializers
from profiles.models.user import User
from profiles.validators.userValidators import PhoneNumberValidator


class CreateUserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=30, required=True, validators=[PhoneNumberValidator()])

    class Meta:
        model = User
        fields = ('name', 'phone_number')


class UserUpdateInfosSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'gender', 'status_code', 'age')


class GetUserInfosForConnectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'phone_number', 'status_code')


# class UserEmailActivationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username')


# class UserGetPublicInfosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('name', 'bio', 'date_joined', 'profile_picture', 'avatar',
#                   'university')


# class UserGetInitialInfosSerializer(serializers.ModelSerializer):
#     # skills = GetSkillsSerializer(many=True, read_only=True)
#     # client_projects = GetProjectsSerializer(many=True, read_only=True)
#     # freelancer_projects = GetProjectsSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'uuid', 'is_active', 'phone_number', 'title', 'bio',
#                   'date_joined', 'profile_picture', 'avatar', 'freelancer_rate', 'client_rate', 'university',
#                   'balance')
