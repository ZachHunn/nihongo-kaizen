from django.contrib import admin

# Register your models here.
from .models import KanjiVocabulary


class KanjiVocabularyAdmin(admin.ModelAdmin):
    list_display = ("kanji", "onyomi", "kunyomi", "kanji_meaning", "example_sentence", "reviewed")


admin.site.register(KanjiVocabulary, KanjiVocabularyAdmin)
