class Vector:
  """
  This class represents a tridimensional vector.
  """
  def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
    _Validator.validate_coordinates([x, y, z])
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, other):
    _Validator.validate_vector(self)
    _validator.validate_vector(other)
    return Vector(
      self.x + other.x, self.y + other.y, self.z + other.z
    )

  def __sub__(self, other):
    _Validator.validate_vector(self)
    _Validator.validate_vector(other)
    return Vector(
      self.x - other.x, self.y - other.y, self.z - other.z
    )

  def __str__(self) -> str:
    return f'[{self.x}, {self.y}, {self.z}]'

  def get(self) -> tuple: return self.x, self.y, self.z

  def set(self, x: float = None, 
          y: float = None, z: float = None) -> None:
    _Validator.validate_coordinates([x, y, z])
    self.x = x if x else self.x
    self.y = x if y else self.y
    self.z = x if z else self.z


class Matrix:
  pass


class _Validator:
  @staticmethod
  def validate_vector(vector: Vector) -> None:
    if not vector:
      raise ValueError("Invalid params.")
    if not isinstance(vector, Vector) or validate_coordinates(vector):
      raise ValueError("Invalid data type.")

  @staticmethod
  def validate_coordinates(vector: Vector | list[float]) -> None:
    if not vector or (
        not isinstance(vector, Vector) and
        not isinstance(vector, list)
    ):
      raise ValueError('Invalid param.')
    if (
          type(vector.x) != 'float' or 
          type(vector.y) != 'float' or 
          type(vector.z) != 'float'
       ) or (
          type(vector[0]) != 'float' or 
          type(vector[1]) != 'float' or 
          type(vector[2]) != 'float'
       ):
      raise ValueError('Invalid param values.')
