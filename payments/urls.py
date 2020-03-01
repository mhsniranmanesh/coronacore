from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from payments.views.transactionView import PerformCashInView, VerifyCashInView

urlpatterns = {
    url(r'^transaction/perform/$', PerformCashInView.as_view(), name="perform-transaction"),
    url(r'^transaction/verify/$', VerifyCashInView.as_view(), name="verify-transaction"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
