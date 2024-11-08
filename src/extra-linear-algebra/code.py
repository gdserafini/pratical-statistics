class Vector:
  """
  This class represents a tridimensional vector.
  """
  def __init__(self, x, y, z) -> None:
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, other):
    Validator(self).validate()
    Validator(other).validate()
    return Vector(
      self.x + other.x, self.y + other.y, self.z + other.z
    )

  def __sub__(self, other):
    Validator(self).validate()
    Validator(other).validate()
    return Vector(
      self.x - other.x, self.y - other.y, self.z - other.z
    )

class Validator:
  _vector: Vector

  def __init__(self, vector: Vector) -> None:
    self._vector = vector

  @staticmethod
  def validate(_vector=None) -> None:
    if not _vector:
      raise ValueError("Invalid params.")
    if not isinstance(_vector, Vector):
      raise ValueError("Invalid data type.")