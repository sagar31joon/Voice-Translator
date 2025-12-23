#pipeline.py : full pipeline which traverses thru all files
from io_layer.mic_stream import MicStream
from core.stt import VoskSTT
from core.translator import HindiEnglishTranslator

class VoiceTranslationPipeline:
    def __init__(self, vosk_model_path):
        self.mic = MicStream()
        self.stt = VoskSTT(vosk_model_path)
        self.translator = HindiEnglishTranslator()

    def run(self):
        print("🎤 Listening... Speak Hindi (Ctrl+C to stop)")
        self.mic.start()

        try:
            while True:
                audio_chunk = self.mic.read()
                hindi_text = self.stt.accept_audio(audio_chunk)

                if hindi_text:
                    english_text = self.translator.translate(hindi_text)
                    print(f"\nHindi: {hindi_text}")
                    print(f"English: {english_text}\n")

        except KeyboardInterrupt:
            print("\nStopping...")
            final_text = self.stt.get_final_text()
            if final_text:
                print("Final Hindi:", final_text)
                print("Final English:", self.translator.translate(final_text))
        finally:
            self.mic.stop()
