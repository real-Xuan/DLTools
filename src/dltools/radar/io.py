from __future__ import annotations

import os
from pathlib import Path

import numpy as np
import scipy.io as sio


def _require_readgssi() -> object:
    try:
        from readgssi import readgssi
    except Exception as exc:  # pragma: no cover - optional dependency
        raise ImportError("readgssi is required. Install with dltools[radar].") from exc
    return readgssi


def read_dzt_file(file_path: str | os.PathLike[str]) -> np.ndarray:
    """Read one .DZT file and return first data array."""
    readgssi = _require_readgssi()
    hdr, arrs, gps = readgssi.readgssi(infile=str(file_path))
    _ = (hdr, gps)
    if not arrs:
        raise ValueError(f"No array payload found in DZT file: {file_path}")
    return arrs[0]


def read_dzt_files_aligned(dir_path: str | os.PathLike[str]) -> np.ndarray:
    """Read all .DZT files in a directory and align them by min width.

    Returns array with shape (rows, cols, slices).
    """
    dirp = Path(dir_path)
    dzt_files = sorted(p for p in dirp.iterdir() if p.suffix.upper() == ".DZT")
    if not dzt_files:
        raise ValueError(f"No .DZT files found under: {dir_path}")

    data_list = [read_dzt_file(p) for p in dzt_files]
    min_length = min(d.shape[1] for d in data_list)
    aligned_data = np.array([d[:, :min_length] for d in data_list])
    aligned_data = np.transpose(aligned_data, (1, 2, 0))
    return aligned_data


def save_array(data: np.ndarray, output_path: str | os.PathLike[str], file_type: str = "mat") -> None:
    """Save radar array as .mat or .npy."""
    out = str(output_path)
    if file_type == "mat":
        sio.savemat(out, {"data": data})
    elif file_type == "npy":
        np.save(out, data)
    else:
        raise ValueError("Unsupported file type. Use 'mat' or 'npy'.")
