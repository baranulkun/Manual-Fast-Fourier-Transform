import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1D FFT 
def fft_1d(x):
    N = len(x)
    if N <= 1:
        return x
    if N % 2 != 0:
        raise ValueError("FFT yalnızca uzunluğu 2'nin bir kuvveti olan diziler için çalışır.")
    
    even = fft_1d(x[0::2])
    odd = fft_1d(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# 1D Inverse FFT 
def ifft_1d(x):
    N = len(x)
    if N <= 1:
        return x
    if N % 2 != 0:
        raise ValueError("IFFT yalnızca uzunluğu 2'nin bir kuvveti olan diziler için çalışır.")
    
    even = ifft_1d(x[0::2])
    odd = ifft_1d(x[1::2])
    T = [np.exp(2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    result = [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]
    return [val / 2 for val in result]

# 2D FFT
def fft_2d(matrix):
    fft_rows = [fft_1d(row) for row in matrix]
    fft_columns = [fft_1d(col) for col in np.transpose(fft_rows)]
    return np.transpose(fft_columns)

# 2D Inverse FFT
def ifft_2d(matrix):
    ifft_rows = [ifft_1d(row) for row in matrix]
    ifft_columns = [ifft_1d(col) for col in np.transpose(ifft_rows)]
    return np.transpose(ifft_columns)

# Zero padding
def pad_to_shape(matrix, target_shape):
    rows, cols = matrix.shape
    
    padded_matrix = np.zeros(target_shape)
    padded_matrix[:rows, :cols] = matrix
    return padded_matrix

# Görüntü yükleme ve normalize etme
def load_and_normalize_image(file_path):
    img = Image.open(file_path).convert('L')  # Griye çevir
    img = np.array(img, dtype=np.float64)
    return (img - np.mean(img)) / np.std(img) #ortalama çıkar ve standart sapmaya böler. Kontrast ve parlaklık farklılıkları için yapılır.

# Görüntü ve şablon yükleme
image = load_and_normalize_image('./images/images.jpg')
template = load_and_normalize_image('./images/images_temp.jpg')

# Zero padding
image_padded = pad_to_shape(image, (256, 256))  # Boyutları 2'nin kuvveti olacak şekilde ayarla
template_padded = pad_to_shape(template, image_padded.shape)  # Şablonu görüntü boyutlarına genişlet

# FFT
image_fft = fft_2d(image_padded)
template_fft = fft_2d(template_padded)

#çapraz güç spe
cross_power_spectrum = (image_fft * np.conj(template_fft)) / np.abs(image_fft * np.conj(template_fft)) 
#konjugantı alır
#frekans tersine döner
#çapraz spektrumunun genliğini
#iki frekans arasında ortak enerjiyi verir.
correlation = ifft_2d(cross_power_spectrum) 

# Korelasyon haritasını normalize et
correlation = np.abs(correlation) 
max_value = np.max(correlation) 
normalized_correlation = np.array([[value / max_value for value in row] for row in correlation])
correlation = normalized_correlation

# En iyi eşleşmeyi bulma
max_loc = np.unravel_index(np.argmax(correlation), correlation.shape)

# Görüntü üzerine eşleşme yerini çizme
top_left = max_loc[::-1]  # Matplotlib için x, y ters çevrildi
h, w = template.shape
bottom_right = (top_left[0] + w, top_left[1] + h)

# Sonuçları görselleştir
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Orijinal Görüntü")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Korelasyon Haritası")
plt.imshow(correlation, cmap='hot')
plt.colorbar()
plt.scatter(max_loc[1], max_loc[0], c='blue', label='En İyi Eşleşme')
plt.legend()

plt.subplot(1, 3, 3)
plt.title("Tahmin Edilen Yer")
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.gca().add_patch(plt.Rectangle(top_left, w, h, edgecolor='green', facecolor='none', lw=2))

plt.tight_layout()
plt.show()
