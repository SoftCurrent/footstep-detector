import sounddevice as sd
from scipy.io.wavfile import write
import os

# Get the folder this script lives in
script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, "test.wav")

duration = 3
sample_rate = 44100

print("Recording in 3... 2... 1...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()

write(save_path, sample_rate, audio)
print("Saved to:", save_path)