from django.contrib.gis.db import models
from django.utils import timezone
import uuid as uuid_lib

from profiles.models.user import User


class UserLocations(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now, blank=False)
    location = models.PointField(db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_locations', blank=True, null=True)
