class Vector:
  """
  This class represents a tridimensional vector.
  """
  def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
    self.x = x
    self.y = y
    self.z = z
    self._validator = _Validator()

  def __add__(self, other):
    self._validator.validate_vector(self)
    self._validator.validate_vector(other)
    return Vector(
      self.x + other.x, self.y + other.y, self.z + other.z
    )

  def __sub__(self, other):
    self._validator.validate_vector(self)
    self._validator.validate_vector(other)
    return Vector(
      self.x - other.x, self.y - other.y, self.z - other.z
    )

  def __str__(self) -> str:
    return f'[{self.x}, {self.y}, {self.z}]'

class Matrix:
  """
  This class represents a mutable matrix.
  """
  def __init__(self, i: int = 1, j: int = 1) -> None:
    self.i = i
    self.j = j
    self.matrix = [[
      0 for _ in range(self._j)]
      for _ in range(self._i)
    ]

  def get(self) -> list[list]:
    return self.matrix

class _Validator:
  @staticmethod
  def validate_vector(vector: Vector) -> None:
    if not vector:
      raise ValueError("Invalid params.")
    if not isinstance(vector, Vector):
      raise ValueError("Invalid data type.")

  @staticmethod
  def validate_matrix(matrix: Matrix) -> None:
    if not matrix:
      raise ValueError("Invalid params.")
    if not isinstance(matrix, Matrix):
      raise ValueError("Invalid data type.")
    if matrix.i <= 0 or matrix.j <= 0:
      raise ValueError("Invalid matrix")
