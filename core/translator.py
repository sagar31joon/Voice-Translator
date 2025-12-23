#translator.py : translates hindi to english
from transformers import pipeline

class HindiEnglishTranslator:
    def __init__(self):
        self.pipe = pipeline("translation_hi_to_en",
                             model = "Helsinki-NLP/opus-mt-hi-en")
    
    def translate(self, text):
        if not text.strip():
            return ""
        result = self.pipe(text)
        return result[0]["translation_text"]

