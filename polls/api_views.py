from rest_framework import viewsets
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.pagination import PageNumberPagination

class QuestionPagination(PageNumberPagination):
    page_size = 5

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes= QuestionSerializer
    pagination_class =QuestionPagination

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    