import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def fft_1d_manual(signal):
    """1D Fourier dönüşümünü manuel olarak hesaplar."""
    N = len(signal)
    result = np.zeros(N, dtype=complex)
    for k in range(N):
        result[k] = np.sum(signal * np.exp(-2j * np.pi * k * np.arange(N) / N))  # Tüm n için toplam
    return result

def fft_2d_manual(image):
    """2D Fourier dönüşümünü manuel olarak hesaplar."""
    # 1D FFT her satır için
    fft_rows = np.zeros_like(image, dtype=complex)
    for i in range(image.shape[0]):
        fft_rows[i, :] = fft_1d_manual(image[i, :])
    
    # 1D FFT her sütun için
    fft_result = np.zeros_like(image, dtype=complex)
    for j in range(image.shape[1]):
        fft_result[:, j] = fft_1d_manual(fft_rows[:, j])

    return fft_result

def fftshift_manual(f):
    """FFT sonucunun frekans sırasını manuel olarak ortalar."""
    rows, cols = f.shape
    f_shifted = np.zeros_like(f)
    f_shifted[:, :cols//2] = f[:, cols//2:]
    f_shifted[:, cols//2:] = f[:, :cols//2]
    temp = np.zeros_like(f_shifted)
    temp[:rows//2, :] = f_shifted[rows//2:, :]
    temp[rows//2:, :] = f_shifted[:rows//2, :]
    return temp

def magnitude_spectrum_manual(fshift):
    """Logaritmik büyüklük spektrumunu hesaplar."""
    return 20 * np.log(np.abs(fshift) + 1)

if __name__ == "__main__":
    # Görseli RGB olarak yükle
    image_path = "./images/witcher.png"  # Görsel yolunu burada belirleyin
    img = Image.open(image_path)
    image = np.array(img)

    # Renk kanallarını ayır
    channels = ['Red', 'Green', 'Blue']
    fft_results = {}
    magnitude_spectrums = {}

    for i, channel in enumerate(channels):
        # Her kanal için 2D Fourier dönüşümü
        fft_result = fft_2d_manual(image[:, :, i])
        fshift = fftshift_manual(fft_result)
        magnitude_spectrum = magnitude_spectrum_manual(fshift)

        # Sonuçları sakla
        fft_results[channel] = fft_result
        magnitude_spectrums[channel] = magnitude_spectrum

    # Görselleştirme
    plt.figure(figsize=(18, 8))

    # Orijinal görüntü
    plt.subplot(2, 2, 1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")

    # Her kanal için büyüklük spektrumu
    for i, channel in enumerate(channels):
        plt.subplot(2, 2, i + 2)
        plt.imshow(magnitude_spectrums[channel], cmap='gray')
        plt.title(f"{channel} Channel Magnitude Spectrum")
        plt.axis("off")

    plt.tight_layout()
    plt.show()
