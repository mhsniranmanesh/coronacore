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


class Connection(models.Model):
    CONNECTION_TYPE_CHOICES = (
        (1, 'Close'),
        (2, 'Normal'),
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now)
    self_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='self_user_connection', blank=False)
    other_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='other_user_connection', blank=False)
    connection_type = models.IntegerField(choices=CONNECTION_TYPE_CHOICES, blank=False, null=False)


class ConnectionRequest(models.Model):
    CONNECTION_TYPE_CHOICES = (
        (1, 'Close'),
        (2, 'Normal'),
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connection_request_user', blank=False)
    phone_number = models.CharField(blank=False, null=False, max_length=50)
    name = models.CharField(blank=True, null=True, max_length=50)
    connection_type = models.IntegerField(choices=CONNECTION_TYPE_CHOICES, blank=False, null=False)
    is_connected = models.BooleanField(default=False, blank=False, null=False)