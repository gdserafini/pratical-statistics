class Vector:
  """
  This class represents a tridimensional vector.
  """
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def _validate(object: Any, object_class: Any) -> None
    if not object or not oclass: 
      raise ValueError("Invalid parans.")
    if not isinstance(object, object_class) 
      raise ValueError("Invalid data type.")

  def __add__(self: Vector, other: Vector) -> Vector:
    self._validate(self, Vector)
    self._validate(other, Vector)
    return Vector(
      self.x + other.x, self.y + other.y, self.z + other.z
    )

  def __sub__(self: Vector, other: Vector) -> Vector:
    self._validate(self, Vector)
    self._validate(other, Vector)
    return Vector(
      self.x - other.x, self.y - other.y, self.z - other.z
    )
