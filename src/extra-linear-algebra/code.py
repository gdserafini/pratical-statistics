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

class _Validator:
  @staticmethod
  def validate(_vector: Vector) -> None:
    if not _vector:
      raise ValueError("Invalid params.")
    if not isinstance(_vector, Vector):
      raise ValueError("Invalid data type.")
    if (_vector.x < 0 or _vector.y < 0 or _vector.z < 0) or\
      (type(_vector.x) != int or type(_vector.y) != int or type(_vector.z) != int):
      raise ValueError("Invalid vector values.")