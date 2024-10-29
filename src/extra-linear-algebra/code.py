class Vector:
  """
  This class represents a tridimensional vector.
  """
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

def _validate_vector(vector: Vector) -> None:
  if not isinstance(vector, Vector) or not vector or\
      not vector.x or not vector.y or not vector.z:
    raise ValueError("Invalid vector.")

def _validate_vectors(vectors: list[Vector]) -> None:
  if not isinstance(vectors, list) or not vectors or len(vectors) <= 0:
    raise ValueError("Invalid vectors.")
  for vector in vectors:
    _validate_vector(vector)

def add(v: Vector, w: Vector) -> Vector:
  """
  Sum two tridimensional vectors.
  :param v: vector1 -> Vector.
  :param w: vector2 -> Vector.
  :return: sum of two vectors -> Vector
  :raise ValueError: if vectors is invalid
  """
  _validate_vector(v)
  _validate_vector(w)
  return Vector(v.x + w.x, v.y + w.y, v.z + w.z)

def add_all(vectors: list[Vector]) -> Vector:
  """
  Return sum of a list of tridimensional vectors.
  :param vectors: list of vectors -> list[Vector]
  :return: sum of all vectors -> Vector
  :raise ValueError: if vectors is invalid
  """
  _validate_vectors(vectors)
  sum_x = sum(v.x for v in vectors)
  sum_y = sum(v.y for v in vectors)
  sum_z = sum(v.z for v in vectors)
  return Vector(sum_x, sum_y, sum_z)

def subtract(v: Vector, w: Vector) -> Vector:
    """
    Subtract one tridimensional vector from another.
    :param v: vector1 -> Vector.
    :param w: vector2 -> Vector.
    :return: difference of the two vectors -> Vector
    :raise ValueError: if vectors are invalid
    """
    _validate_vector(v)
    _validate_vector(w)
    return Vector(v.x - w.x, v.y - w.y, v.z - w.z)

def subtract_all(vectors: list[Vector]) -> Vector:
    """
    Subtract all vectors of a list of tridimensional vectors.
    :param vectors: list of vectors -> list[Vector]
    :return: subtract of all vectors -> Vector
    :raise ValueError: if vectors is invalid
    """
    _validate_vectors(vectors)
    result = vector[0]
    for vector in vectors[1:]:
        result = subtract(result, vector)
    return vector
