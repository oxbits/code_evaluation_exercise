from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import (
    QuestionSet,
    Question,
    Answer,
    Image,
)
from .serializers import (
    QuestionSetSerializer,
    QuestionSerializer,
    AnswerSerializer,
    ImageSerializer,
) 

# # Create your views here.

class QuestionSetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = QuestionSet.objects.all()
    serializer_class = QuestionSetSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

