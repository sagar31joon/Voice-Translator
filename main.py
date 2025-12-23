#main.py
from core.pipeline import VoiceTranslationPipeline

if __name__ == "__main__":
    pipeline = VoiceTranslationPipeline("models/vosk/vosk-small-hi")
    pipeline.run()
