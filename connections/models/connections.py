from django.contrib.gis.db import models
import uuid as uuid_lib

from django.utils import timezone

from profiles.models.user import User


class Contact(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user_contacts', blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True, max_length=50)
    name = models.CharField(blank=True, null=True, max_length=50)