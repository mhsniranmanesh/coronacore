from rest_framework import serializers

from payments.models.transaction import CashIn


class PerformCashInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashIn
        fields = ['amount', 'port', 'reason']


class VerifyCashInSerializer(serializers.Serializer):
    status = serializers.IntegerField(required=True, allow_null=False)
    transId = serializers.IntegerField(required=True, allow_null=False)
    mobile = serializers.IntegerField(required=False)
    factorNumber = serializers.CharField(required=True, allow_null=False)
    cardNumber = serializers.CharField(required=False, allow_null=True)
    message = serializers.CharField(required=False, allow_null=True)
    description = serializers.CharField(required=False, allow_null=True)


class BuyWishcoinSerializer(serializers.Serializer):
    PACKAGE_CHOICES = (1, 2, 3)
    package = serializers.ChoiceField(PACKAGE_CHOICES)