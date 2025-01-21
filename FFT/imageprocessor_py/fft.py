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

def ifft_1d_manual(signal):
    """1D Ters Fourier dönüşümünü manuel olarak hesaplar."""
    N = len(signal)
    result = np.zeros(N, dtype=complex)
    for n in range(N):
        result[n] = np.sum(signal * np.exp(2j * np.pi * n * np.arange(N) / N))  # Tüm k için toplam
    return result / N

def fft_2d_manual(image):
    """2D Fourier dönüşümünü manuel olarak hesaplar."""
    fft_rows = np.zeros_like(image, dtype=complex)
    for i in range(image.shape[0]):
        fft_rows[i, :] = fft_1d_manual(image[i, :])
    fft_result = np.zeros_like(image, dtype=complex)
    for j in range(image.shape[1]):
        fft_result[:, j] = fft_1d_manual(fft_rows[:, j])
    return fft_result

def rgb_to_grayscale_manual(image):
    """
    RGB görüntüyü manuel olarak gri tonlamaya çevirir.
    Formül: Gray = 0.299 * R + 0.587 * G + 0.114 * B
    """
    # Görüntüyü NumPy dizisine çevir
    image_array = np.array(image)
    
    # RGB kontrolü
    if len(image_array.shape) == 3 and image_array.shape[2] == 3:
        r, g, b = image_array[:, :, 0], image_array[:, :, 1], image_array[:, :, 2]
        grayscale = 0.299 * r + 0.587 * g + 0.114 * b  # Gri tonlama dönüşüm formülü
        return grayscale.astype(np.uint8)  # Değerleri 0-255 arasında tut
    else:
        raise ValueError("Görüntü RGB formatında değil.")
    
def ifft_2d_manual(frequency_image):
    """2D Ters Fourier dönüşümünü manuel olarak hesaplar."""
    ifft_rows = np.zeros_like(frequency_image, dtype=complex)
    for i in range(frequency_image.shape[0]):
        ifft_rows[i, :] = ifft_1d_manual(frequency_image[i, :])
    ifft_result = np.zeros_like(frequency_image, dtype=complex)
    for j in range(frequency_image.shape[1]):
        ifft_result[:, j] = ifft_1d_manual(ifft_rows[:, j])
    return np.real(ifft_result)

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

# Fourier işlemleri için sınıf
class FourierProcessor:
    def __init__(self, transformed_image):
        self.transformed_image = transformed_image

    def inverse_fourier(self):
        """Ters Fourier dönüşümünü uygular."""
        return ifft_2d_manual(self.transformed_image)

if __name__ == "__main__":
    image_path = "./images/ist.jpg"  # Görsel yolunu burada belirleyin
    img = Image.open(image_path)  # Görseli yükle
    image = rgb_to_grayscale_manual(img)  # Gri tonlamaya çevir

    # 2D Fourier dönüşümünü hesapla
    fft_result = fft_2d_manual(image)

    # Fourier büyüklük spektrumunu hesapla
    fshift = fftshift_manual(fft_result)
    magnitude_spectrum = magnitude_spectrum_manual(fshift)

    # Fourier işlemleri sınıfına gönder
    processor = FourierProcessor(fft_result)
    reconstructed_image = processor.inverse_fourier()

    # Görselleştirme
    plt.figure(figsize=(18, 6))

    # Orijinal görüntü
    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")

    # Fourier büyüklük spektrumu
    plt.subplot(1, 3, 2)
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title("Fourier Magnitude Spectrum")
    plt.axis("off")

    # Ters Fourier dönüşümünden elde edilen görüntü
    plt.subplot(1, 3, 3)
    plt.imshow(reconstructed_image, cmap='gray')
    plt.title("Reconstructed Image (Inverse FFT)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
