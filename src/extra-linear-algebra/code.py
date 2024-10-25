class Vector:
  def get(self) -> tuple: pass

class Vector2D(Vector):
  def __init__(self,
               x1: int, x2: int,
               y1: int, y2: int) -> None:
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2

    def get(self) -> tuple:
      return self._x1, self._y1, self._x2, self._y2

class VectorOperator:
  def add(self, v: Vector, w: Vector) -> Vector: pass

class Vector2DOperator(VectorOperator):
  pass