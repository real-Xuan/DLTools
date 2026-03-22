from __future__ import annotations

import numpy as np

from dltools.utils import optional_import


def random_flip(image: np.ndarray, horizontal: bool = True, vertical: bool = False) -> np.ndarray:
    """Deterministic flip operator with explicit directions."""
    out = np.asarray(image)
    if horizontal:
        out = np.fliplr(out)
    if vertical:
        out = np.flipud(out)
    return out.copy()


def random_rotate90(image: np.ndarray, k: int = 1) -> np.ndarray:
    """Rotate image by k * 90 degrees."""
    return np.rot90(np.asarray(image), k=k).copy()


def albumentations_augment(image: np.ndarray, transform_name: str = "HorizontalFlip", p: float = 1.0) -> np.ndarray:
    """Run a named Albumentations transform (optional dependency)."""
    albu = optional_import("albumentations", "pip install dltools[cv]")
    transform_cls = getattr(albu, transform_name, None)
    if transform_cls is None:
        raise ValueError(f"Unknown albumentations transform: {transform_name}")
    transform = transform_cls(p=p)
    result = transform(image=np.asarray(image))
    return result["image"]
