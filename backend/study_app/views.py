from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import KanjiVocabularySerializer
from .models import KanjiVocabulary


class KanjiVocabularyView(viewsets.ModelViewSet):
    serializer_class = KanjiVocabularySerializer
    queryset = KanjiVocabulary.objects.all()