from typing import Any


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


def sum_vectors(vectors: list[Vector]) -> Vector:
    vector_sum = Vector([0,0,0])
    for vector in vectors:
        vector_sum = vector_sum + vector
    return vector_sum
