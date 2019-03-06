from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from questions import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'question_set', views.QuestionSetViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'image', views.ImageViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

