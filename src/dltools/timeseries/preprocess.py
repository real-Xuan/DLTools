from __future__ import annotations

import numpy as np


def zscore_scale(x: np.ndarray, eps: float = 1e-8) -> np.ndarray:
    arr = np.asarray(x, dtype=np.float64)
    mean = arr.mean(axis=0, keepdims=True)
    std = arr.std(axis=0, keepdims=True)
    return (arr - mean) / (std + eps)


def minmax_scale(x: np.ndarray, eps: float = 1e-8) -> np.ndarray:
    arr = np.asarray(x, dtype=np.float64)
    x_min = arr.min(axis=0, keepdims=True)
    x_max = arr.max(axis=0, keepdims=True)
    return (arr - x_min) / (x_max - x_min + eps)


def robust_scale(x: np.ndarray, eps: float = 1e-8) -> np.ndarray:
    arr = np.asarray(x, dtype=np.float64)
    median = np.median(arr, axis=0, keepdims=True)
    q1 = np.percentile(arr, 25, axis=0, keepdims=True)
    q3 = np.percentile(arr, 75, axis=0, keepdims=True)
    return (arr - median) / (q3 - q1 + eps)
