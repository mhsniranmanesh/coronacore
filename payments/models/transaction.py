import uuid
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from profiles.models.user import User


class CashIn(models.Model):
    PORT_CHOICES = (
        (1, 'Pay.ir'),
    )
    REASON_CHOICES = (
        (1, 'balance'),
        (2, 'donate')
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cash_ins')
    trans_id = models.IntegerField(blank=True, null=True, db_index=True)
    amount = models.PositiveIntegerField(blank=False,
                                         validators=[MinValueValidator(10000), MaxValueValidator(50000000)])
    date_created = models.DateTimeField(default=timezone.now)
    date_applied = models.DateTimeField(blank=True, null=True)
    card_number = models.CharField(blank=True, max_length=30)
    factor_number = models.CharField(blank=False, max_length=15, db_index=True)
    message = models.CharField(blank=True, max_length=300)
    is_applied = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    reason = models.SmallIntegerField(blank=False, choices=REASON_CHOICES)
    port = models.SmallIntegerField(blank=False, choices=PORT_CHOICES)

