from rest_framework import serializers

from profiles.models.user import User


class UserUpdateLocationSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    class Meta:
        model = User
        fields = ('latitude', 'longitude')