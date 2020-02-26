from django.contrib.gis.db import models
import uuid as uuid_lib


class Question(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    text = models.CharField(max_length=10000, blank=False)
    rank = models.IntegerField(blank=False, null=False)


class QuestionDetail(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('video', 'Video'),
        ('image', 'Image'),
        ('none', 'None')
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    media_type = models.CharField(blank=True, choices=MEDIA_TYPE_CHOICES, max_length=10)
    url = models.URLField(max_length=1000, null=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name="question_details")
    text = models.CharField(max_length=10000, blank=True, null=True)


class QuestionOption(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    text = models.CharField(max_length=10000, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_options")
    rank = models.IntegerField(blank=False, null=False)