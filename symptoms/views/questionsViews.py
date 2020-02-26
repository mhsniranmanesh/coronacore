from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from symptoms.models.questions import Question
from symptoms.serializers.questionsSerializers import GetQuestionSerializer


class GetAllQuestionsView(ListAPIView):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = GetQuestionSerializer


