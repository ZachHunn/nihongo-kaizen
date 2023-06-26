from rest_framework import serializers
from .models import KanjiVocabulary

class KanjiVocabularySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = KanjiVocabulary
        fields = ('kanji', 'onyomi', 'kunyomi', 'kanji_meaning', 'example_sentence', 'reviewed')

