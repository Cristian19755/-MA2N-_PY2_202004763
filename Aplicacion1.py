import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt
import wave

def generate_audio(data, filename, sample_rate=44100):
    with wave.open(filename, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(4)
        f.setframerate(sample_rate)
        f.writeframes(data.tobytes())

def apply_effect(filename, effect):
    with wave.open(filename, "rb") as f:
        params = f.getparams()
        data = np.frombuffer(f.readframes(params.nframes), dtype=np.int32)

    modified_data = effect(data)

    plt.plot(modified_data, label="Efecto aplicado")
    plt.plot(data, label="Función original")
    plt.title("Efecto aplicado vs función original")
    plt.legend()
    plt.show()

    generate_audio(modified_data, "output.wav", params.framerate)

def echo(data):
    delay = 10000  
    decay = 2

    modified_data = data.copy()

    for i in range(delay, len(data)):
        modified_data[i] += int(data[i - delay] * decay)

    return modified_data

if __name__ == "__main__":
    filename = "dark-drill-piano-melody_120bpm.wav"
    effect = echo
    apply_effect(filename, effect)

