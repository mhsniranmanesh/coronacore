from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from symptoms.views.questionsViews import GetAllQuestionsView
from symptoms.views.responsesViews import SendAllResponsesView

urlpatterns = {
    url(r'^questions/all/$', GetAllQuestionsView.as_view(), name="get-all-questions"),
    url(r'^responses/all/$', SendAllResponsesView.as_view(), name="send-all-questions"),
}
urlpatterns = format_suffix_patterns(urlpatterns)