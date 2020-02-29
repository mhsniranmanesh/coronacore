from rest_framework import serializers

from connections.models.connections import Contact, ConnectionRequest
from profiles.models.user import User
from profiles.serializers.userSerializers import GetUserInfosForConnectionsSerializer


class ConnectionsAddContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'phone_number')


class ConnectionsRequestConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionRequest
        fields = ('phone_number', 'type')


class GetUserConnectionRequestsSerializer(serializers.ModelSerializer):
    user = GetUserInfosForConnectionsSerializer()
    class Meta:
        model = ConnectionRequest
        fields = ('user', 'type', 'is_connected')


class ConnectionsAcceptConnectionSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(allow_null=False)
    class Meta:
        model = User
        fields = ['uuid']
