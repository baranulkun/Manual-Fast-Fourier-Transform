package imageprocessor_java;

import java.util.Arrays;

public class FourierTransform {

    public static void main(String[] args) {

        // Örnek giriş matrisi
        double[][] inputImage = {
                { 1, 5, 4, 3, 5 },
                { 2, 4, 5, 5, 3 },
                { 2, 1, 5, 2, 3 },
                { 1, 2, 2, 2, 4 },
                { 5, 5, 1, 7, 5 }
        };

        int height = inputImage.length;
        int width = inputImage[0].length;

        // Fourier bileşenlerini tutacak matrisler
        double[][] realPart = new double[height][width];
        double[][] imagPart = new double[height][width];
        double[][] magnitude = new double[height][width];

        // 2D Fourier Transform
        for (int u = 0; u < height; u++) {
            for (int v = 0; v < width; v++) {
                double sumReal = 0;
                double sumImag = 0;

                for (int x = 0; x < height; x++) {
                    for (int y = 0; y < width; y++) {
                        double angle = 2 * Math.PI * ((double) u * x / height + (double) v * y / width);
                        sumReal += inputImage[x][y] * Math.cos(angle);
                        sumImag -= inputImage[x][y] * Math.sin(angle);
                    }
                }

                realPart[u][v] = sumReal;
                imagPart[u][v] = sumImag;
                magnitude[u][v] = Math.sqrt(sumReal * sumReal + sumImag * sumImag);
            }
        }

        // Sonuçları yazdır
        System.out.println("Real Part:");
        printMatrix(realPart);

        System.out.println("Imaginary Part:");
        printMatrix(imagPart);

        System.out.println("Magnitude:");
        printMatrix(magnitude);
    }

    // Matris yazdırma fonksiyonu
    public static void printMatrix(double[][] matrix) {
        for (double[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
