from __future__ import annotations

import math

import numpy as np

try:
    import cv2
except Exception:  # pragma: no cover - optional runtime dependency
    cv2 = None


def generate_kernel(size: int = 15) -> np.ndarray:
    """Generate a simple horizontal motion blur kernel."""
    if size < 1:
        raise ValueError("size must be >= 1")
    kernel_motion_blur = np.zeros((size, size), dtype=np.float64)
    kernel_motion_blur[int((size - 1) / 2), :] = np.ones(size, dtype=np.float64)
    return kernel_motion_blur / float(size)


def generate_psf(length: int, angle: float) -> tuple[np.ndarray, tuple[int, int]]:
    """Generate point spread function for arbitrary motion angle."""
    if length < 1:
        raise ValueError("length must be >= 1")

    eps = np.finfo(float).eps
    alpha = (angle - math.floor(angle / 180.0) * 180.0) / 180.0 * math.pi
    cosalpha = math.cos(alpha)
    sinalpha = math.sin(alpha)
    half = length / 2.0

    if cosalpha < 0:
        xsign = -1
    elif angle == 90:
        xsign = 0
    else:
        xsign = 1

    psfwdt = 1
    sx = int(abs(length * cosalpha + psfwdt * xsign - length * eps))
    sy = int(abs(length * sinalpha + psfwdt - length * eps))
    sx = max(1, sx)
    sy = max(1, sy)

    psf = np.zeros((sy, sx), dtype=np.float64)

    for i in range(sy):
        for j in range(sx):
            psf[i][j] = i * abs(cosalpha) - j * sinalpha
            rad = math.sqrt(i * i + j * j)
            if rad >= half and abs(psf[i][j]) <= psfwdt:
                if abs(cosalpha) < eps:
                    temp = 0.0
                else:
                    temp = half - abs((j + psf[i][j] * sinalpha) / cosalpha)
                psf[i][j] = math.sqrt(psf[i][j] * psf[i][j] + temp * temp)
            psf[i][j] = psfwdt + eps - abs(psf[i][j])
            if psf[i][j] < 0:
                psf[i][j] = 0

    anchor = (0, 0)
    if 0 < angle < 90:
        psf = np.fliplr(psf)
        anchor = (psf.shape[1] - 1, 0)
    elif -90 < angle < 0:
        psf = np.flipud(np.fliplr(psf))
        anchor = (psf.shape[1] - 1, psf.shape[0] - 1)
    elif angle < -90:
        psf = np.flipud(psf)
        anchor = (0, psf.shape[0] - 1)

    denom = psf.sum()
    if denom <= 0:
        raise ValueError("generated PSF has zero sum; check length/angle inputs")
    psf = psf / denom
    return psf, anchor


def motion_blur(image: np.ndarray, length: int = 15, angle: float = 0.0) -> np.ndarray:
    """Apply motion blur to an image using OpenCV filter2D."""
    if cv2 is None:
        raise ImportError("opencv-python is required for motion_blur. Install with dltools[cv].")
    kernel, anchor = generate_psf(length=length, angle=angle)
    return cv2.filter2D(image, -1, kernel, anchor=anchor)
