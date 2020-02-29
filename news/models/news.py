from django.contrib.gis.db import models
import uuid as uuid_lib

from django.utils import timezone


class Feed(models.Model):
    FEED_TYPE_CHOICES = (
        (1, 'Report'),
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now)
    feed_type = models.IntegerField(choices=FEED_TYPE_CHOICES, default=1, blank=False)
    url = models.URLField(blank=True, null=True, max_length=200)
    title = models.CharField(blank=False, max_length=1000)
    details = models.CharField(blank=True, null=True, max_length=10000)
    priority = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

