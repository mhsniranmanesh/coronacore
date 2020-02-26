from django.contrib import admin
from symptoms.models.questions import Question, QuestionDetail, QuestionOption


admin.site.register(Question)
admin.site.register(QuestionOption)
admin.site.register(QuestionDetail)
