package imageprocessor_java;

import java.util.Arrays;

public class InverseFourierTransform {

    public static void main(String[] args) {
        // Fourier dönüşümü ile elde edilen veriler (örnek olarak manuel tanımlandı)
        double[][] realPart = {
                { 70, -7.72, -3.68, -3.68, -7.72 },
                { 5.44, 4.20, -4.90, 1.34, 1.52 },
                { -3.28, -5.92, 2.02, -1.79, -0.52 },
                { -3.28, -0.52, -1.79, 2.02, -5.92 },
                { 5.44, 1.52, 1.34, -4.90, 4.20 }
        };

        double[][] imagPart = {
                { 0, -6.23, -9.89, 9.89, 6.23 },
                { 0.90, 0.22, 5.19, 6.39, 2.78 },
                { 0.99, -4.12, 6.28, 3.48, -1.63 },
                { -0.99, 1.63, -3.48, -6.28, 4.12 },
                { -0.90, -2.78, -6.39, -5.19, -0.22 }
        };

        int height = realPart.length;
        int width = realPart[0].length;

        // Orijinal görüntüyü tutacak matris
        double[][] reconstructedImage = new double[height][width];

        // 2D Inverse Fourier Transform
        for (int x = 0; x < height; x++) {
            for (int y = 0; y < width; y++) {
                double sumReal = 0;

                for (int u = 0; u < height; u++) {
                    for (int v = 0; v < width; v++) {
                        double angle = 2 * Math.PI * ((double) u * x / height + (double) v * y / width);
                        double realComponent = realPart[u][v] * Math.cos(angle) - imagPart[u][v] * Math.sin(angle);
                        sumReal += realComponent;
                    }
                }

                // Normalize ederek orijinal piksel değerini hesapla
                reconstructedImage[x][y] = sumReal / (width * height);
            }
        }

        // Sonuçları yazdır
        System.out.println("Reconstructed Image:");
        printMatrix(reconstructedImage);
    }

    // Matris yazdırma fonksiyonu
    public static void printMatrix(double[][] matrix) {
        for (double[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
