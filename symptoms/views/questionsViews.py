from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from symptoms.models.questions import Question
from symptoms.serializers.questionsSerializers import GetQuestionSerializer


class GetAllQuestionsView(ListAPIView):
    queryset = Question.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = GetQuestionSerializer
