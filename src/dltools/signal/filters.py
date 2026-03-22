from __future__ import annotations

import numpy as np
from scipy import signal


def _validate_1d(x: np.ndarray) -> np.ndarray:
    arr = np.asarray(x, dtype=np.float64)
    if arr.ndim != 1:
        raise ValueError("input signal must be 1D")
    return arr


def _butterworth(cutoff: float | tuple[float, float], fs: float, btype: str, order: int = 4) -> tuple[np.ndarray, np.ndarray]:
    nyq = 0.5 * fs
    if btype == "band":
        if not isinstance(cutoff, tuple) or len(cutoff) != 2:
            raise ValueError("band cutoff must be a (low, high) tuple")
        wn = (cutoff[0] / nyq, cutoff[1] / nyq)
    else:
        if isinstance(cutoff, tuple):
            raise ValueError("single cutoff expected for low/high pass")
        wn = cutoff / nyq
    return signal.butter(order, wn, btype=btype)


def lowpass_filter(x: np.ndarray, cutoff: float, fs: float, order: int = 4) -> np.ndarray:
    """Apply low-pass Butterworth filter."""
    arr = _validate_1d(x)
    b, a = _butterworth(cutoff, fs, btype="low", order=order)
    return signal.filtfilt(b, a, arr)


def highpass_filter(x: np.ndarray, cutoff: float, fs: float, order: int = 4) -> np.ndarray:
    """Apply high-pass Butterworth filter."""
    arr = _validate_1d(x)
    b, a = _butterworth(cutoff, fs, btype="high", order=order)
    return signal.filtfilt(b, a, arr)


def bandpass_filter(x: np.ndarray, low_cut: float, high_cut: float, fs: float, order: int = 4) -> np.ndarray:
    """Apply band-pass Butterworth filter."""
    arr = _validate_1d(x)
    if low_cut >= high_cut:
        raise ValueError("low_cut must be smaller than high_cut")
    b, a = _butterworth((low_cut, high_cut), fs, btype="band", order=order)
    return signal.filtfilt(b, a, arr)


def moving_average(x: np.ndarray, window: int = 5) -> np.ndarray:
    """Simple moving average smoother."""
    arr = _validate_1d(x)
    if window < 1:
        raise ValueError("window must be >= 1")
    if window == 1:
        return arr.copy()
    kernel = np.ones(window, dtype=np.float64) / float(window)
    return np.convolve(arr, kernel, mode="same")
