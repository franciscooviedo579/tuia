# Practica 1 - Programacion Orientada a Objetos - Programacion II - TUIA

""" representación de un punto en un plano cartesiano 2D """
class Point:

  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return '(' + str(self.x) + ', ' + str(self.y) + ')'
  
  def __eq__(self, other) -> bool:
    if not isinstance(other, Point):
      return NotImplemented
    return self.x == other.x and self.y == other.y
  
  def __add__(self, other: 'Point') -> 'Point':
    return Point(self.x + other.x, self.y + other.y)
  
class Rectangle:
  def __init__(self, width: float, height: float, corner: Point) -> None:
    self.width = width
    self.height = height
    self.corner = corner

  def __str__(self) -> None:
    return '(' + str(self.width) + ',' + str(self.height) + ',' + str(self.corner) + ')'
  
  def __eq__(self, other) -> bool:
    return ( 
      self.width == other.width and
      self.height == other.height and
      self.corner == other.corner
    )
  
punto = Point(5,5)
rectangulo = Rectangle(10,20,punto)
rectangulo2 = Rectangle(12,20,punto)
