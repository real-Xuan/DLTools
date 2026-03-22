from __future__ import annotations

from importlib import import_module


def optional_import(module_name: str, install_hint: str) -> object:
    """Import optional dependency with a consistent error message."""
    try:
        return import_module(module_name)
    except Exception as exc:  # pragma: no cover
        raise ImportError(f"Optional dependency '{module_name}' is required. Install with: {install_hint}") from exc
