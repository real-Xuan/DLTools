from __future__ import annotations

import re
import unicodedata


_PUNCT_RE = re.compile(r"[^\w\s]+", flags=re.UNICODE)


def normalize_text(text: str, lowercase: bool = True, normalize_form: str = "NFKC") -> str:
    """Normalize unicode text and optionally lowercase."""
    out = unicodedata.normalize(normalize_form, text)
    if lowercase:
        out = out.lower()
    return out.strip()


def remove_punctuation(text: str) -> str:
    """Remove punctuation while preserving whitespace and alphanumeric chars."""
    return _PUNCT_RE.sub("", text)
