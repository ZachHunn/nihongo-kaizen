from django.db import models


# Create your models here.
class KanjiVocabulary(models.Model):
    kanji = models.CharField(max_length=150, null=False)
    onyomi = models.CharField(max_length=150, null=True)
    kunyomi = models.CharField(max_length=150, null=True)
    kanji_meaning = models.CharField(max_length=150, null=False)
    example_sentence = models.CharField(max_length=150, null=False)
    reviewed = models.BooleanField(default=False)
