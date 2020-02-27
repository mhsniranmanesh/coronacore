from rest_framework import serializers


class SendResponseSerializer(serializers.Serializer):
    question_id = serializers.UUIDField(allow_null=False)
    option_id = serializers.UUIDField(allow_null=False)


class SendAllResponsesSerializer(serializers.Serializer):
    question_responses = SendResponseSerializer(many=True)
