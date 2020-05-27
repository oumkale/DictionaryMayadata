import json
from .models import Dictionary

def add_words():
    with open('words.json') as f:
        data = json.load(f)
        for word,meaning in data.items():
            Dictionary.objects.get_or_create(word=word,meaning=meaning)