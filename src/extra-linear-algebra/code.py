class Vector:
  def __init__(self, 
              x1: int, y1: int, z1: int 
              x2: int, y2: int, z2: int) -> None:
    self._x1 = x1
    self._y1 = y1
    self._z1 = z1
    self._x2 = x2
    self._y2 = y2
    self._z2 = z2

  def get() -> tuple:
    return (
      self._x1, self._y1, self._z1
      self._x2, self._y2, self._z2
    )
