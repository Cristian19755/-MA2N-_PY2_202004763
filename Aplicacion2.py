import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt
import wave

def compress_audio(filename, compression_ratio=0.5):

    with wave.open(filename, "rb") as f:
        params = f.getparams()
        data = np.frombuffer(f.readframes(params.nframes), dtype=np.int32)

    fft_data = fft.fft(data)

    fft_data = fft_data[0:int(len(fft_data) * compression_ratio)]

    inverse_fft_data = fft.ifft(fft_data)

    data_normalized = data / max(abs(data))
    inverse_fft_data_normalized = inverse_fft_data / max(abs(inverse_fft_data))

    output_filename = "output_compressed.wav"  
    generate_audio(inverse_fft_data_normalized, output_filename, params.framerate)

    plt.figure(figsize=(10, 5))  
    plt.plot(inverse_fft_data_normalized, label="funcion comprimida")
    plt.plot(data_normalized, label="Función original")
    plt.title("Funcion comprimida vs función original")
    plt.legend()
    plt.show()

    print(f"Archivo de audio comprimido guardado como {output_filename}")

def generate_audio(data, filename, sample_rate):
    with wave.open(filename, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(4)
        f.setframerate(sample_rate)
        f.writeframes(data.astype(np.int32).tobytes())

if __name__ == "__main__":
    filename = "dark-drill-piano-melody_120bpm.wav"
    compression_ratio = 0.5  
    compress_audio(filename, compression_ratio)
