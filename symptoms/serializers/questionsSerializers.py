from rest_framework import serializers
from symptoms.models.questions import Question, QuestionOption, QuestionDetail


class GetQuestionOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ['uuid', 'text', 'rank']


class GetQuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionDetail
        fields = ['uuid', 'media_type', 'url', 'text']


class GetQuestionSerializer(serializers.ModelSerializer):
    question_details = GetQuestionDetailSerializer(allow_null=True)
    question_options = GetQuestionOptionsSerializer(many=True, allow_null=True)

    class Meta:
        model = Question
        fields = ('uuid', 'text', 'rank', 'question_details', 'question_options')