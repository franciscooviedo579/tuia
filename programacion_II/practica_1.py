# Practica 1 - Programacion Orientada a Objetos - Programacion II - TUIA

# Ejercicio 1

# 1.

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
  
  def distancia(self, other: 'Point') -> float:
    return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** (1/2)
    
  
class Rectangle:
  def __init__(self, width: float, height: float, corner: Point) -> None:
    self.width = width
    self.height = height
    self.corner = corner

  def __str__(self) -> None:
    return '(' + str(self.width) + ',' + str(self.height) + ',' + str(self.corner) + ')'
  
  def __eq__(self, other) -> bool:
    if not isinstance(other, Point):
      return NotImplemented
    return ( 
      self.width == other.width and
      self.height == other.height and
      self.corner == other.corner
    )


# 2.

#  Defina una función llamada mover_rectángulo que tome un rectángulo y dos parámetros dx y
# dy. Esta función debería cambiar de posición el rectángulo sumando dx a la coordenada x de la
# esquina superior izquierda y del mismo modo sumar dy a la coordenada y de la esquina superior
# izquierda. Haga las dos versiones, una función pura y una función modificadora.

import copy


def mover_rectangulo_modificadora(rect: Rectangle, dx: float, dy: float) -> None:
  """
  Funcion modificadora mover rectangulo
  """
  rect.corner.x = rect.corner.x + dx
  rect.corner.y = rect.corner.y + dy

def mover_rectangulo_pura(rect: Rectangle, dx: float, dy: float) -> Rectangle:
  """
  Funcion pura mover rectangulo
  """
  newRect = copy.deepcopy(rect)

  newRect.corner.x = newRect.corner.x + dx
  newRect.corner.y = newRect.corner.y + dy

  return newRect

punto = Point(5,5)
rectangulo = Rectangle(10,20,punto)
rectangulo2 = Rectangle(12,20,punto)

#mover_rectangulo_modificadora(rectangulo,5,5)

""" print(rectangulo)
print(mover_rectangulo_pura(rectangulo,5,5)) """


# 3.

#  Escriba código para crear algunas instancias de puntos y rectángulos y pruebe los métodos y
# funciones que escribió.

def main():
  width = int(input("Ingrese el ancho del Rectangulo:\n"))
  height = int(input("Ingrese el alto del Rectangulo:\n"))
  pointX = int(input("Ingrese la coordenada x:\n"))
  pointY = int(input("Ingrese la coordenada y:\n"))

  punto = Point(pointX, pointY)
  rectangulo = Rectangle(width, height, punto)
  dx = -1
  dy = -1

  while(dx != 0 and dy != 0):
    print("Ingrese los parametros para mover el rectangulo \n - Ingrese ambos parametros en 0 para salir")
    dx = int(input("Ingrese el parametro x:\n"))
    dy = int(input("Ingrese el parametro y:\n"))
    mover_rectangulo_modificadora(rectangulo, dx, dy)
    print(f"El rectangulo se movio a {rectangulo}")


""" main() """

# Ejercicio 2

# Defina, en la clase Point, un método distancia() que nos de la distancia euclídea entre dos puntos.
punto1 = Point(1,4)
punto2 = Point(4,5)

""" d = punto1.distancia(punto2)
print(f"La distancia entre los puntos {punto1} y {punto2} es {d}") """


