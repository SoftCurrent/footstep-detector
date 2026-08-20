import librosa
import librosa.display
import matplotlib.pyplot as plt

audio_path = "/Users/liamsmollan/Desktop/Footstep Detector/test.wav"

# Load the audio file
y, sr = librosa.load(audio_path, sr=None)
stft = librosa.stft(y)

# Construct a figure and axes object:
waveform_fig, waveform_ax = plt.subplots()

# Plot on the axes:
librosa.display.waveshow(y, sr=sr, ax=waveform_ax)
waveform_ax.set(title="Test Audio Waveform")

# Spectogram Plot
spectrogram_fig, axes = plt.subplots(nrows=2, sharex=True)
img = librosa.display.specshow(stft, vscale="dBFS",
                               sr=sr, hop_length=512, x_axis="time", y_axis="hz", ax=axes[0])
spectrogram_fig.colorbar(img, ax=axes[0], label="dBFS")
axes[0].set(title="Spectrogram")
axes[0].label_outer()
librosa.display.waveshow(y, sr=sr, ax=axes[1])
axes[1].set(title="Time-domain")

plt.show()
