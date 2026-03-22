from __future__ import annotations

import numpy as np
from scipy import signal

from dltools.utils import optional_import


def spectrogram(waveform: np.ndarray, fs: int, nperseg: int = 512, noverlap: int = 256) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute magnitude spectrogram via scipy STFT."""
    x = np.asarray(waveform, dtype=np.float64).ravel()
    freqs, times, zxx = signal.stft(x, fs=fs, nperseg=nperseg, noverlap=noverlap)
    mag = np.abs(zxx)
    return freqs, times, mag


def zero_crossing_rate(waveform: np.ndarray) -> float:
    """Compute global zero crossing rate."""
    x = np.asarray(waveform, dtype=np.float64).ravel()
    if x.size < 2:
        return 0.0
    signs = np.signbit(x)
    crossings = np.count_nonzero(signs[:-1] != signs[1:])
    return float(crossings / (x.size - 1))


def mfcc_librosa(waveform: np.ndarray, fs: int, n_mfcc: int = 13) -> np.ndarray:
    """MFCC extraction through librosa (optional dependency)."""
    librosa = optional_import("librosa", "pip install dltools[audio]")
    x = np.asarray(waveform, dtype=np.float64).ravel()
    return librosa.feature.mfcc(y=x, sr=fs, n_mfcc=n_mfcc)
