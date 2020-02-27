from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from symptoms.models.questions import Question, QuestionOption
from symptoms.models.responses import UserResponse
from symptoms.serializers.responsesSerializers import SendAllResponsesSerializer


class SendAllResponsesView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = SendAllResponsesSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = request.user
                if len(serializer.validated_data['question_responses']) > 100:
                    return Response(data={'message': 'maximum acceptable batch size is 100'},
                                    status=status.HTTP_400_BAD_REQUEST)
                for response in serializer.validated_data['question_responses']:
                    try:
                        question_id = response['question_id']
                        option_id = response['option_id']
                        question = Question.objects.get(uuid=question_id)
                        option = QuestionOption.objects.get(uuid=option_id)
                        response = UserResponse(user=user, question=question, option=option)
                        response.save()

                    except Exception as e:
                        continue
                return Response(data={'message': 'success'}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response(data={'message': 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)