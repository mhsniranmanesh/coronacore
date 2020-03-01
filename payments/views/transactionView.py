from math import ceil

from django.shortcuts import redirect
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from pay_ir.api.client import PayIrClient

from coronacore.settings import PAY_IR_API_KEY, PAY_IR_REDIRECT_ADDRESS
from payments.models.transaction import CashIn
from payments.serializers.transactionSerializer import PerformCashInSerializer, VerifyCashInSerializer
from payments.utils.transactionUtils import unique_factor_generator

pay_client = PayIrClient(PAY_IR_API_KEY)


class PerformCashInView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PerformCashInSerializer(data=request.data)
        if serializer.is_valid():
            try:
                factor_number = unique_factor_generator()
                user = request.user
                cash_in = CashIn(user=user,
                                 factor_number=factor_number,
                                 amount=serializer.validated_data['amount'],
                                 port=serializer.validated_data['port'],
                                 reason=serializer.validated_data['reason']
                                 )
                cash_in.save()
                pay_data = pay_client.init_transaction(serializer.validated_data['amount'],
                                                       PAY_IR_REDIRECT_ADDRESS,
                                                       cash_in.factor_number)

                cash_in.trans_id = pay_data['trans_id']
                cash_in.is_applied = True
                cash_in.date_applied = timezone.now()
                cash_in.save()

                return Response({'payment_url': pay_data['payment_url']}, status=status.HTTP_201_CREATED)
            except:
                return Response(data={'message': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCashInView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = VerifyCashInSerializer(data=request.data)
        if serializer.is_valid():
            try:
                trans_status = int(serializer.validated_data['status'])
                transId = int(serializer.validated_data['transId'])

                if trans_status == 0:
                    cash_in = CashIn.objects.get(trans_id=transId)
                    cash_in.message = serializer.validated_data['message']
                    cash_in.save()
                    url = '127.0.0.1:8080/payment/?status=%s&factor_number=%s' % (0, cash_in.factor_number)
                    return redirect(url)

                else:
                    cash_in = CashIn.objects.get(trans_id=transId)
                    if cash_in.is_verified:
                        url = '127.0.0.1:8080/payment/?status=%s&factor_number=%s' % (2, cash_in.factor_number)
                        return redirect(url)

                    verify_data = pay_client.verify_transaction(transId)
                    amount = ceil(int(verify_data)/10000)
                    cash_in.amount = amount
                    cash_in.is_verified = True
                    if cash_in.reason == CashIn.BALANCE:
                        user = cash_in.user
                        user.balance += amount
                        user.save()

                    cash_in.save()
                    url = '127.0.0.1:8080/payment/?status=%s&factor_number=%s' % (1, cash_in.factor_number)
                    return redirect(url)

            except:
                url = '127.0.0.1:8080/payment/?status=3'
                return redirect(url)

        url = '127.0.0.1:8080/payment/?status=4'
        return redirect(url)
