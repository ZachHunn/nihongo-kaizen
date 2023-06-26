from django.test import TestCase
from study_app.models import KanjiVocabulary
# Create your tests here.


class KanjiVocabularyTestCase(TestCase):
    def setUp(self) -> None:
        KanjiVocabulary.objects.create(kanji='test', onyomi='onyomi', kunyomi='kunyomi', kanji_meaning='meaning', example_sentence='example', reviewed=False)

    def test_kanji_vocab_is_created(self):
        kanji_vocab = KanjiVocabulary.objects.get(kanji="test")
        self.assertEqual(kanji_vocab.kanji, "kanji")