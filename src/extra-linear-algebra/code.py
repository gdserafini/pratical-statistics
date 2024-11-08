class Vector:
  """
  This class represents a tridimensional vector.
  """
  def __init__(self, x, y, z) -> None:
    self.x = x
    self.y = y
    self.z = z
    _validator = _Validator()

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

class _Validator:
  @staticmethod
  def validate(_vector: Vector) -> None:
    if not _vector:
      raise ValueError("Invalid params.")
    if not isinstance(_vector, Vector):
      raise ValueError("Invalid data type.")
