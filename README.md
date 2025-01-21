# Manual Implementation of 2D Fourier Transform in Python

## Description
This project manually implements the 2D Fourier Transform in Python to analyze and reconstruct images without using built-in FFT functions. It covers grayscale conversion, frequency spectrum visualization, and inverse transformation for image reconstruction.

## Features
- **Manual 1D Fourier Transform:** Computes the discrete Fourier transform manually without relying on existing libraries.
- **Manual 2D Fourier Transform:** Applies the 1D Fourier Transform row-wise and column-wise to achieve 2D transformation.
- **Manual Inverse Fourier Transform:** Reconstructs the image from the frequency domain using the inverse Fourier transform.
- **Manual Image Processing:** Converts RGB images to grayscale without external libraries.
- **Fourier Magnitude Spectrum Visualization:** Visualizes the magnitude spectrum using logarithmic scaling.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/baranulkun/Manual-Fast-Fourier-Transform.git
   cd Manual-Fast-Fourier-Transform
   ```

2. Install dependencies:
   ```bash
   pip install numpy matplotlib pillow
   ```

3. Run the script:
   ```bash
   python fft.py
   ```

## Usage

1. Place your image inside the `images/` folder.
2. Modify the `image_path` in the script to point to your image.
3. Run the script to visualize the original, frequency spectrum, and reconstructed images.

## Example Output

- **Original Image**
- **Fourier Magnitude Spectrum**
- **Reconstructed Image (Inverse FFT)**

## License
This project is licensed under the MIT License.

## Author
- Your Name
- Contact: your.email@example.com

## Contributing
Feel free to contribute by opening issues or submitting pull requests.

