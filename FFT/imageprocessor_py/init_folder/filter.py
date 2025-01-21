import numpy as np

def apply_frequency_filter(img, filter_func):
    """
    Frekans alanında özelleştirilmiş bir filtre uygular.
    
    :param img: Girdi gri tonlamalı görüntü.
    :param filter_func: Frekans alanını değiştiren fonksiyon.
    :return: Filtrelenmiş görüntü.
    """
    # Görüntünün DFT'sini hesapla
    dft = np.fft.fft2(img)
    dft_shift = np.fft.fftshift(dft)

    # Filtreyi uygula
    filtered_dft_shift = filter_func(dft_shift)

    # Ters DFT ile tekrar uzaysal alana dön
    filtered_dft = np.fft.ifftshift(filtered_dft_shift)
    filtered_img = np.fft.ifft2(filtered_dft)

    # Gerçek kısmını döndür
    return np.abs(filtered_img)


def low_pass_filter(dft_shift, radius):
    """
    Düşük geçiren filtre uygular.
    
    :param dft_shift: Frekans alanındaki kaydırılmış DFT.
    :param radius: Kesme frekansı yarıçapı.
    :return: Filtrelenmiş frekans alanı.
    """
    rows, cols = dft_shift.shape
    crow, ccol = rows // 2, cols // 2

    # Düşük geçiren filtre için maske oluştur
    mask = np.zeros((rows, cols), dtype=np.float32)
    y, x = np.ogrid[:rows, :cols]
    mask_area = (x - ccol)**2 + (y - crow)**2 <= radius**2
    mask[mask_area] = 1

    return dft_shift * mask


def high_pass_filter(dft_shift, radius):
    """
    Yüksek geçiren filtre uygular.
    
    :param dft_shift: Frekans alanındaki kaydırılmış DFT.
    :param radius: Kesme frekansı yarıçapı.
    :return: Filtrelenmiş frekans alanı.
    """
    rows, cols = dft_shift.shape
    crow, ccol = rows // 2, cols // 2

    # Yüksek geçiren filtre için maske oluştur
    mask = np.ones((rows, cols), dtype=np.float32)
    y, x = np.ogrid[:rows, :cols]
    mask_area = (x - ccol)**2 + (y - crow)**2 <= radius**2
    mask[mask_area] = 0

    return dft_shift * mask
