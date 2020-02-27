from django.contrib.gis.db import models
import uuid as uuid_lib

from django.utils import timezone

from profiles.models.user import User
from symptoms.models.questions import Question, QuestionOption


class UserResponse(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="response_question")
    option = models.ForeignKey(QuestionOption, on_delete=models.CASCADE, related_name="response_option")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_response")