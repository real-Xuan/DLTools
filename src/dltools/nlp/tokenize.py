from __future__ import annotations

import re

from dltools.utils import optional_import

_WORD_RE = re.compile(r"\b\w+\b", flags=re.UNICODE)


def basic_tokenize(text: str) -> list[str]:
    """Regex-based lightweight tokenizer."""
    return _WORD_RE.findall(text)


def nltk_tokenize(text: str) -> list[str]:
    """Use NLTK tokenizer when available."""
    nltk = optional_import("nltk", "pip install dltools[nlp]")
    tokenizer = getattr(nltk.tokenize, "word_tokenize", None)
    if tokenizer is None:
        raise ImportError("nltk.tokenize.word_tokenize is not available")
    return tokenizer(text)
