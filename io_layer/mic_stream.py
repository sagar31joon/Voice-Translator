#mic_stream.py : gets input from user
import sounddevice as sd
import queue

class MicStream:
    def __init__(self, samplerate=16000, blocksize=8000):
        self.samplerate = samplerate
        self.blocksize = blocksize
        self.q = queue.Queue()

    def _callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.q.put(bytes(indata))

    def start(self):
        self.stream = sd.RawInputStream(
            samplerate=self.samplerate,
            blocksize=self.blocksize,
            dtype="int16",
            channels=1,
            callback=self._callback
        )
        self.stream.start()

    def read(self):
        return self.q.get()

    def stop(self):
        self.stream.stop()
        self.stream.close()
