# Generated by Django 4.2 on 2023-04-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KanjiVocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kanji', models.CharField(max_length=150)),
                ('kana', models.CharField(max_length=150)),
                ('kanji_meaning', models.CharField(max_length=150)),
                ('example_sentence', models.CharField(max_length=150)),
                ('reviewed', models.BooleanField(default=False)),
            ],
        ),
    ]
