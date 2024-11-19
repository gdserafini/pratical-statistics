class Vector:
  """
  This class represents a tridimensional vector.
  """
  def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
    self._validator = _Validator()
    self._validator.validate_types([x, y, z], float)
    self.x = x
    self.y = y
    self.z = z

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

  def get(self) -> tuple: return (self.x, self.y, self.z)

  def set(self, x: float = None, 
          y: float = None, z: float = None) -> None:
    _validator.validate_types([x, y, z], float)
    self.x = x if x else self.x
    self.y = x if y else self.y
    self.z = x if z else self.z


class Matrix:
  """
  This class represents a mutable matrix.
  """
  def __init__(self, matrix: list[list] = None, i: int = 0, j: int = 0) -> None:
    self._validator = Validator()
    self.validator.validate_types(matrix, float)
    self.i = i
    self.j = j
    self.matrix = matrix if matrix else\
    [[
      0 for _ in range(self._j)]
      for _ in range(self._i)
    ]

  def get(self) -> list[list]: return self.matrix

  def set(self, matrix: list[list] = None) -> None:
    self.validator.validate_types(matrix, float)
    self.matrix = matrix if matrix else self.matrix


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
    if matrix.i < 0 or matrix.j < 0 or not matrix.matrix:
      raise ValueError("Invalid matrix")

  @staticmethod
  def validate_types(values: list[Any], type: Any) -> None:
    if not values or not type: 
      raise ValueError('Invalid params.')
    if isinstance(values, list[list]):
      for line in values:
        for value in lines:
          if not value or not isinstance(value, type):
            raise ValueError('Invalid data type.')
    else:
      for values in values:
        if not value or not isinstance(value, type):
          raise ValueError('Invalid data type.')
