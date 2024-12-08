from typing import Any
from collections.abc import Iterable


class Vector:
    def __init__(self, values: list[Any]) -> None:
        self._values = values

    def get(self): return self._values

    def __add__(self, other: Any) -> Any:
        return Vector(
            [xa + xb for xa, xb in zip(self._values, other.get())]
        )

    def __sub__(self, other: Any) -> Any:
        return Vector(
            [xa - xb for xa, xb in zip(self._values, other.get())]
        )

    def __str__(self): return str(self._values)

    def __mul__(self, scalar) -> Any:
        return Vector([scalar * v for v in self._values])

    def __rmul__(self, scalar) -> Any: return self.__mul__(scalar)


def vsum(vectors: Iterable) -> Vector:
    vector_sum = Vector([0,0,0])
    for vector in vectors:
        vector_sum = vector_sum + vector
    return vector_sum


def vmean(vectors: Iterable) -> Vector:
    _sum = vsum(vectors)
    _len = len(list(vectors))
    return 1/_len * _sum
