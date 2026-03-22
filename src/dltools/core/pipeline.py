from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable


class Operator(ABC):
    """Base callable operator used by pipeline composition."""

    @abstractmethod
    def __call__(self, data: Any) -> Any:
        raise NotImplementedError


class Pipeline:
    """Minimal composable pipeline for chaining operators or callables."""

    def __init__(self, name: str = "pipeline") -> None:
        self.name = name
        self._ops: list[Callable[[Any], Any]] = []

    def add(self, op: Callable[[Any], Any]) -> "Pipeline":
        self._ops.append(op)
        return self

    def __call__(self, data: Any) -> Any:
        result = data
        for op in self._ops:
            result = op(result)
        return result
