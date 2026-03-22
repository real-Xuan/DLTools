from __future__ import annotations

import numpy as np


def rolling_std(x: np.ndarray, window: int = 10) -> np.ndarray:
    arr = np.asarray(x, dtype=np.float64)
    if arr.ndim != 1:
        raise ValueError("rolling_std currently supports 1D input")
    if window < 2:
        raise ValueError("window must be >= 2")
    out = np.zeros_like(arr)
    half = window // 2
    for i in range(arr.shape[0]):
        left = max(0, i - half)
        right = min(arr.shape[0], i + half + 1)
        out[i] = np.std(arr[left:right])
    return out


def trend_slope(x: np.ndarray) -> float:
    arr = np.asarray(x, dtype=np.float64).ravel()
    if arr.size < 2:
        return 0.0
    idx = np.arange(arr.size, dtype=np.float64)
    slope, _ = np.polyfit(idx, arr, deg=1)
    return float(slope)
