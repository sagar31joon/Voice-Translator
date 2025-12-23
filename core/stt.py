#stt.py : transcribes input audio
import json
from vosk import Model, KaldiRecognizer

class VoskSTT:
    def __init__(self, model_path, samplerate=16000):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, samplerate)
        self.recognizer.SetWords(True)

    def accept_audio(self, audio_bytes):
        """
        Feed audio bytes to recognizer.
        Returns (final_text or None)
        """
        if self.recognizer.AcceptWaveform(audio_bytes):
            result = json.loads(self.recognizer.Result())
            return result.get("text", "")
        return None

    def get_final_text(self):
        result = json.loads(self.recognizer.FinalResult())
        return result.get("text", "")
