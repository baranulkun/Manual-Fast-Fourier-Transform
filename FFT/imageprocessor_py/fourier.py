import math
import numpy as np
import matplotlib.pyplot as plt  # Görselleştirme için gerekli

def main():
    # Örnek giriş matrisi
    input_image = [
        [1, 5, 4, 3, 5],
        [2, 4, 5, 5, 3],
        [2, 1, 5, 2, 3],
        [1, 2, 2, 2, 4],
        [5, 5, 1, 7, 5]
    ]

    height = len(input_image)
    width = len(input_image[0])

    # Fourier bileşenlerini tutacak matrisler
    real_part = np.zeros((height, width))
    imag_part = np.zeros((height, width))
    magnitude = np.zeros((height, width))

    # 2D Fourier Transform
    for u in range(height):
        for v in range(width):
            sum_real = 0
            sum_imag = 0

            for x in range(height):
                for y in range(width):
                    angle = 2 * math.pi * ((u * x / height) + (v * y / width))
                    sum_real += input_image[x][y] * math.cos(angle)
                    sum_imag -= input_image[x][y] * math.sin(angle)

            real_part[u][v] = sum_real
            imag_part[u][v] = sum_imag
            magnitude[u][v] = math.sqrt(sum_real**2 + sum_imag**2)

    # Sonuçları yazdır
    print("Real Part:")
    print_matrix(real_part)

    print("Imaginary Part:")
    print_matrix(imag_part)

    print("Magnitude:")
    print_matrix(magnitude)

    # Görselleştirme
    visualize_results(input_image, real_part, imag_part, magnitude)

# Matris yazdırma fonksiyonu
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Görselleştirme fonksiyonu
def visualize_results(input_image, real_part, imag_part, magnitude):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    # Orijinal görüntü
    axes[0, 0].imshow(input_image, cmap='gray')
    axes[0, 0].set_title("Input Image")
    axes[0, 0].axis("off")

    # Real Part
    axes[0, 1].imshow(real_part, cmap='gray')
    axes[0, 1].set_title("Real Part")
    axes[0, 1].axis("off")

    # Imaginary Part
    axes[1, 0].imshow(imag_part, cmap='gray')
    axes[1, 0].set_title("Imaginary Part")
    axes[1, 0].axis("off")

    # Magnitude
    axes[1, 1].imshow(magnitude, cmap='gray')
    axes[1, 1].set_title("Magnitude")
    axes[1, 1].axis("off")

    # Görselleştirme ekranını göster
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
