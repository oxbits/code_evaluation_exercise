from rest_framework import serializers
from .models import (
    QuestionSet,
    Question,
    Answer,
    Image,
)


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    votes = serializers.SerializerMethodField()

    def get_votes(self, obj):
        return {
                'YES': len(Answer.objects.filter(question=obj, text='Y')),
                'NO': len(Answer.objects.filter(question=obj, text='N')),
                'TOTAL': len(Answer.objects.filter(question=obj)),
        }

    class Meta:
        model = Question
        fields = (
            'url',
            'id',
            'text',
            'token',
            'question_set',
            'order',
            'votes',
        )


class EmbeddedQuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = (
            'url',
            'id',
            'text',
            'token',
            'order',
        )


class QuestionSetSerializer(serializers.HyperlinkedModelSerializer):

    set_question = EmbeddedQuestionSerializer(many=True, read_only=True)
    votes = serializers.SerializerMethodField()

    def get_votes(self, obj):
        return {
            i.token: {
                'YES': len(Answer.objects.filter(question=i, text='Y')),
                'NO': len(Answer.objects.filter(question=i, text='N')),
                'TOTAL': len(Answer.objects.filter(question=i)),
            } for i in Question.objects.filter(question_set=obj.id)
        }

    class Meta:
        model = QuestionSet
        depth = 1
        fields = (
            'url',
            'id',
            'set_name',
            'set_question',
            'votes'
        )


class AnswerSerializer(serializers.HyperlinkedModelSerializer):

    # question = QuestionSerializer(many=False, read_only=True)

    class Meta:
        model = Answer
        fields = (
            'url',
            'id',
            'text',
            'question',
        )


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    # answer = AnswerSerializer(many=False, read_only=False)

    class Meta:
        model = Image
        fields = (
            'url',
            'id',
            'file',
            'answer',
        )
