#translator.py : translates hindi to english
from transformers import pipeline
import os
from transformers import (
    pipeline,
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

class HindiEnglishTranslator:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-hi-en", local_dir="models/transformer/opus-mt-hi-en"):
        self.model_name = model_name
        self.local_dir = local_dir
        if os.path.exists(local_dir,):
            tokenizer = AutoTokenizer.from_pretrained(local_dir)
            model = AutoModelForSeq2SeqLM.from_pretrained(local_dir)
        else:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

            os.makedirs(local_dir, exist_ok=True)
            tokenizer.save_pretrained(local_dir)
            model.save_pretrained(local_dir)
            
        self.pipe = pipeline(task = "translation_hi_to_en",
                             model = model,
                             tokenizer = tokenizer)
    
    def translate(self, text):
        if not text.strip():
            return ""
        result = self.pipe(text)
        return result[0]["translation_text"]

