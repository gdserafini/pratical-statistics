class Vector:
  """
  This class represents a tridimensional vector.
  """
  def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
    self.x = x
    self.y = y
    self.z = z
    self._validator = _Validator()

  def __add__(self, other):
    self._validator.validate(self)
    self._validator.validate(other)
    return Vector(
      self.x + other.x, self.y + other.y, self.z + other.z
    )

  def __sub__(self, other):
    self._validator.validate(self)
    self._validator.validate(other)
    return Vector(
      self.x - other.x, self.y - other.y, self.z - other.z
    )

  def __str__(self) -> str:
    return f'[{self.x}, {self.y}, {self.z}]'

class Matrix:
  """
  This class represents a mutable matrix.
  """
  pass

class _Validator:
  @staticmethod
  def validate_vector(vector: Vector) -> None:
    if not vector:
      raise ValueError("Invalid params.")
    if not isinstance(vector, Vector):
      raise ValueError("Invalid data type.")
    if (vector.x < 0 or vector.y < 0 or vector.z < 0) or\
      (type(vector.x) != int or type(vector.y) != int or type(vector.z) != int):
      raise ValueError("Invalid vector values.")
