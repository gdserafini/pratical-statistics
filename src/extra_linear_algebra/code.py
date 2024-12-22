from typing import Any
from collections.abc import Iterable
from enum import Enum


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


class PAxis(Enum):
    X = [1, 0, 0]
    Y = [0, 1, 0]
    Z = [0, 0, 1]


class VectorOperator:
    @staticmethod
    def vsum(vectors: Iterable) -> Vector:
        vector_sum = Vector([0,0,0])
        for vector in vectors:
            vector_sum = vector_sum + vector
        return vector_sum

    @staticmethod
    def vmean(vectors: Iterable) -> Vector:
        _sum = VectorOperator.vsum(vectors)
        _len = len(list(vectors))
        return 1/_len * _sum

    @staticmethod
    def dot(v: Vector, w: Vector) -> float:
        return sum(vi * wi for vi, wi in zip(v.get(), w.get()))

    @staticmethod
    def projection(vector: Vector, axis: PAxis = PAxis.X) -> float:
        return VectorOperator.dot(vector, Vector(axis.value))

    @staticmethod
    def sum_of_squares(vector: Vector) -> float:
        return VectorOperator.dot(vector, vector)
