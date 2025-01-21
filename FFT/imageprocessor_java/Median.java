package imageprocessor_java;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.Arrays;
import javax.imageio.ImageIO;
import javax.swing.*;

public class Median {
    // kenar dolgusu yap
    // her bir nokta için median al
    public static void main(String[] args) {
        try {
            String imagePath = "./images/images.jpg";
            BufferedImage originalImage = ImageIO.read(new File(imagePath));

            int width = originalImage.getWidth();
            int height = originalImage.getHeight();

            BufferedImage modifiedImage = cerceveOlustur(width, height, originalImage);
            System.out.println("Görsel Genişliği: " + width);
            System.out.println("Görsel Yüksekliği: " + height);
            BufferedImage lastImg = median(width + 2, height + 2, modifiedImage);

            displayImage(originalImage, modifiedImage, lastImg);

            File output = new File("./images/output/output_image.jpg");
            ImageIO.write(modifiedImage, "jpg", output);
            System.out.println("Değiştirilmiş görsel output_image.jpg olarak kaydedildi.");
        } catch (Exception e) {
            System.out.println("Hata: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static BufferedImage median(int width, int height, BufferedImage img) {
        BufferedImage resultImg = new BufferedImage(width, height, img.getType());

        for (int i = 1; i < width - 1; i++) {
            for (int j = 1; j < height - 1; j++) {
                int[] red = new int[9];
                int[] green = new int[9];
                int[] blue = new int[9];

                int index = 0;
                for (int x = -1; x <= 1; x++) {
                    for (int y = -1; y <= 1; y++) {
                        int rgb = img.getRGB(i + x, j + y);
                        red[index] = (rgb >> 16) & 0xFF;
                        green[index] = (rgb >> 8) & 0xFF;
                        blue[index] = rgb & 0xFF;
                        index++;
                    }
                }

                // Sort the arrays to find the median
                Arrays.sort(red);
                Arrays.sort(green);
                Arrays.sort(blue);

                // Get the median value (the 5th element after sorting)
                int medianRed = red[4];
                int medianGreen = green[4];
                int medianBlue = blue[4];

                int medianRgb = (0xFF << 24) | (medianRed << 16) | (medianGreen << 8) | medianBlue;
                resultImg.setRGB(i, j, medianRgb);
            }
        }

        return resultImg;
    }

    public static BufferedImage cerceveOlustur(int width, int height, BufferedImage img) {
        width += 2;
        height += 2;

        BufferedImage newImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                newImage.setRGB(i, j, Color.BLACK.getRGB());
            }
        }
        for (int i = 1; i < img.getWidth(); i++) {
            for (int j = 1; j < img.getHeight(); j++) {
                newImage.setRGB(i, j, img.getRGB(i - 1, j - 1));
            }
        }

        return newImage;
    }

    private static void displayImage(BufferedImage originalImage, BufferedImage modifiedImage, BufferedImage lastImg) {
        JFrame frame = new JFrame();
        frame.setSize(1000, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(null);
        panel.setSize(1000, 420);
        panel.setBackground(Color.white);
        frame.add(panel);

        JLabel label_org = new JLabel(new ImageIcon(originalImage));
        JLabel label_mod = new JLabel(new ImageIcon(modifiedImage));
        JLabel label_last = new JLabel(new ImageIcon(lastImg));

        label_org.setBounds(50, 50, originalImage.getWidth(), originalImage.getHeight());
        panel.add(label_org);

        label_mod.setBounds(350, 50, modifiedImage.getWidth(), originalImage.getHeight());
        panel.add(label_mod);

        label_last.setBounds(650, 50, lastImg.getWidth(), originalImage.getHeight());
        panel.add(label_last);

        frame.setVisible(true);
    }
}
