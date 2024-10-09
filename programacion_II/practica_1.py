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

"""  Defina una función llamada mover_rectángulo que tome un rectángulo y dos parámetros dx y
 dy. Esta función debería cambiar de posición el rectángulo sumando dx a la coordenada x de la
 esquina superior izquierda y del mismo modo sumar dy a la coordenada y de la esquina superior
 izquierda. Haga las dos versiones, una función pura y una función modificadora. """

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


# Ejercicio 3

"""   
 Defina la clase Automovil que contenga (al menos) los siguientes atributos:
  • patente (string)
  • marca (string)
  • kilometros_recorridos (float)
  • litros_nafta (float)
  La clase deberá proveer un constructor que permita inicializar los atributos, siendo obligatorios patente
y marca. kilometros_recorridos y litros_nafta, se pueden especificar o no. Si no se especifican,
se inicializarán por defecto en 0.
La clase tendrá además un método llamado avanzar() que recibirá como argumento el número de
kilómetros a conducir y sumará los kilómetros recorridos al valor del atributo kilometros_recorridos.
El método también restará al valor de litros_nafta la cantidad consumida (se calcula el consumo de
gasolina como 8.8 litros por cada 100 kms recorridos).
La clase también contendrá otro método llamado cargar_nafta() que recibirá como argumento los
litros introducidos que deberán sumarse a la variable litros_nafta.
Por último, será necesario controlar que el método avanzar nunca obtendrá un número negativo en la
gasolina. En dicho caso, deberá mostrar el siguiente mensaje: "Es necesario cargar nafta para
recorrer la cantidad indicada de kilómetros". 
"""

class Automovil:

  def __init__(self, patente: str, marca: str, consumoPor100KM: float, kilometros_recorridos: float = 0, litros_nafta: float = 0) -> None:
    self.patente = patente
    self.marca = marca
    self.kilometros_recorridos = kilometros_recorridos
    self.litros_nafta = litros_nafta
    self.consumoPor100KM = consumoPor100KM

  def avanzar(self, kmConducir: float) -> None:
    NAFTA_NECESARIA = (kmConducir * self.consumoPor100KM) / 100

    if(self.litros_nafta < NAFTA_NECESARIA):
      print("Es necesario cargar nafta para recorrer la cantidad indicada de kilómetros")
    else:
      self.kilometros_recorridos += kmConducir
      self.litros_nafta -= (kmConducir * self.consumoPor100KM) / 100

  def cargar_nafta(self, litros: float) -> None:
    self.litros_nafta += litros


""" Renault = Automovil("AA123BB", "Renault", 8.8, 100000, 45)

Renault.avanzar(50)
print(Renault.kilometros_recorridos)
print(Renault.litros_nafta)

Renault.cargar_nafta(23)

Renault.avanzar(50)
print(Renault.kilometros_recorridos)
print(Renault.litros_nafta) """


# Ejercicio 4 y 5
class Robot:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.historial = ""

  def mueve(self, movimientos: str) -> None:

    for movimiento in movimientos:
      match movimiento:
        case 'A' | 'a':
          self.y += 1
          self.historial += movimiento
        case 'R' | 'r':
          self.y -= 1
          self.historial += movimiento
        case 'I' | 'i':
          self.x -= 1
          self.historial += movimiento
        case 'D' | 'd':
          self.x += 1
          self.historial += movimiento
        case _:
          print(f"{movimiento} Movimiento no valido")
  
  def posicion_actual(self) -> str:
    return f"El robot se encuentra en ({self.x, self.y})"
  
  def obtener_historico_de_movimiento(self) -> str:
    return self.historial
  
  def como_volver(self) -> str:
    EJE_X = self.x * 'I' if self.x > 0 else abs(self.x) * 'D'
    EJE_Y = self.y * 'R' if self.y > 0 else abs(self.y) * 'A'

    return f"Necesita {len(EJE_X)} movimiento/s {EJE_X} en el Eje X y {len(EJE_Y)} movimiento/s {EJE_Y} en el Eje Y"


mi_robot = Robot()
orden = input("Introduce la orden: ")

while orden != 'fin':
  mi_robot.mueve(orden)
  print(mi_robot.posicion_actual())
  orden = input("Ingrese la orden, 'fin' para salir: ")

print(mi_robot.obtener_historico_de_movimiento())
print(mi_robot.como_volver())






