from typing import Any


class Vector:
    def __init__(self, values: list[Any]) -> None:
        self._values = values

    def get(self): return self._values

    def _validate_vector(self, vector: Any) -> None:
        if len(self._values) != len(vector.get()) or\
                not isinstance(vector, Vector):
            raise ValueError('Invalid vector')

    def __add__(self, other: Any) -> Any:
        self._validate_vector(other)
        return Vector(
            [xa + xb for xa, xb in zip(self._values, other.get())]
        )

    def __sub__(self, other: Any) -> Any:
        self._validate_vector(other)
        return Vector(
            [xa - xb for xa, xb in zip(self._values, other.get())]
        )

    def __str__(self): return str(self._values)
