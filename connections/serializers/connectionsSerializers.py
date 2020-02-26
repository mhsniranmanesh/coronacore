from rest_framework import serializers

from connections.models.connections import Contact


class ConnectionsAddContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'phone_number')