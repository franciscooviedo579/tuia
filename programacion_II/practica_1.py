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


""" mi_robot = Robot()
orden = input("Introduce la orden: ")

while orden != 'fin':
  mi_robot.mueve(orden)
  print(mi_robot.posicion_actual())
  orden = input("Ingrese la orden, 'fin' para salir: ")

print(mi_robot.obtener_historico_de_movimiento())
print(mi_robot.como_volver()) """

# Ejercicio 6

""" 
Crear las clases Materia y Carrera.
Cada materia tiene: - Un código de materia. - Un nombre de la materia. - Una cantidad de créditos
que aporta.
Una carrera puede pensarse como una lista de materias.
"""

class Materia:
  def __init__(self, codigoMat: str, nombreMat: str, creditosMat: int) -> None:
    self.codigoMat = codigoMat
    self.nombreMat = nombreMat
    self.creditosMat = creditosMat

class Carrera:
  """
  Lista de materias
  """
  def __init__(self, materias: list[Materia]) -> None:
    self.materias = materias
    self.creditos = 0
    self.promedio = None
    self.materiasAprobadas = []

  def __str__(self) -> str:
    return f"Créditos: {self.creditos} -- Promedio: {self.calc_promedio()} -- Materias aprobadas: {self.print_materias_aprobadas()}"
  
  def add_creditos(self, materia: Materia) -> None :
    self.creditos += materia.creditosMat

  def calc_promedio(self) -> float | str:
    if(len(self.materiasAprobadas) == 0): return "N/A"
    totalAprobadas = len(self.materiasAprobadas)
    totalNotas = 0
    for materiaAprobada in self.materiasAprobadas:
      nota = materiaAprobada["nota"]
      totalNotas += nota

    return totalNotas / totalAprobadas

    # for materia in materiasAprobadas:

  def aprobar(self, codigoMat: str, nota: float) -> None:
    
    for materia in self.materias:
      if(materia.codigoMat == codigoMat):
        self.materiasAprobadas.append({"materia": materia, "nota": nota})
        self.creditos += materia.creditosMat
        return
    
    print(f"Error la materia {codigoMat} no es parte del plan de estudios.")
  
  def print_materias_aprobadas(self) -> str:

    materiasAprob = ""
    if(len(self.materiasAprobadas) == 0): return materiasAprob

    for materia in self.materiasAprobadas:
      nota = materia["nota"]
      infoMateria = materia["materia"]
      materiasAprob += f"{infoMateria.codigoMat} {infoMateria.nombreMat} ({nota}) "
    
    return materiasAprob

# --- Comportamiento esperado ---  
""" analisis2 = Materia("61.03", "Análisis 2", 8)
fisica2 = Materia("62.01", "Física 2", 8)
algo1 = Materia("75.40", "Algoritmos 1", 6)
c = Carrera([analisis2, fisica2, algo1])
print(c) """
#Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
""" c.aprobar("95.14", 7) """
#Error: La materia 75.14 no es parte del plan de estudios
""" c.aprobar("75.40", 10)
c.aprobar("62.01", 7)
print(c) """
#Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas: 75.40 Algoritmos 1 (10) 62.01 Física 2 (7)


# Ejercicio 7

""" Encontrar los errores en el siguiente código y proponer soluciones: """
""" 
class Cosa:
  def __init__(self, valor):
    self.valor = valor

class Coleccion:
  def __init__(self):
    self.coleccion = []
  def agregar_cosa(cosa: Cosa):
    coleccion.append(cosa) # No se paso self como parametro y a coleccion le falta self.coleccion

cosa = Cosa() # No se pasa parametro para inicializar valor
coleccion = Coleccion()
coleccion.agregar_cosa(cosa) """
  
class Cosa:
  def __init__(self, valor):
    self.valor = valor

class Coleccion:
  def __init__(self):
    self.coleccion = []
  def agregar_cosa(self, cosa: Cosa):
    self.coleccion.append(cosa)

""" cosa = Cosa(123)
coleccion = Coleccion()
coleccion.agregar_cosa(cosa)  

print(coleccion.coleccion) """

# Ejercicio 8

""" 
  Programe un conjunto de seis clases que modele esta taxonomía utilizando clases. Luego, agregue un
método speak a cada clase imprimiendo un mensaje apropiado a cada clase (por ejemplo, una instancia
de animal podría imprimir "Soy un animal").
Luego, agregue un método talk a la clase Animal, que simplemente delegue el funcionamiento en
speak. ¿Qué ocurre al llamar a talk en una subclase? ¿Qué ocurre si borramos el método speak de la
clase Hacker?
"""

class Animal:
  def __init__(self, nombre: str) -> None:
    self.nombre = nombre
  
  def talk(self) -> None:
    self.speak()

  def speak(self) -> None:
    print("Soy un animal")
    
class Mamiferos(Animal):
  def __init__(self, nombre: str) -> None:
    super().__init__(nombre)
  
  def speak(self) -> None:
    print("Soy un mamifero")

  
class Felinos(Mamiferos):
  def __init__(self, nombre: str) -> None:
    super().__init__(nombre)
  
  def speak(self) -> None:
    print("Soy un felino")

  
class Canidos(Mamiferos):
  def __init__(self, nombre: str) -> None:
    super().__init__(nombre)
  
  def speak(self) -> None:
    print("Soy un canido")

  
class Primates(Mamiferos):
  def __init__(self, nombre: str) -> None:
    super().__init__(nombre)
  
  def speak(self) -> None:
    print("Soy un primate")

  
class Hacker(Primates):
  def __init__(self, nombre: str) -> None:
    super().__init__(nombre)
  
  def speak(self) -> None:
    print("Soy un Kaker")


""" animal = Animal("Animal")
mamifero = Mamiferos("Mamifero")
felino = Felinos("Felino")
canido = Canidos("Canido")
primate = Primates("Primate")
hacker = Hacker("Hacker")

animal.speak()
mamifero.speak()
felino.speak()
canido.speak()
primate.speak()
hacker.speak()

hacker.talk() """

# Ejercicio 9

""" 
Complete la funcionalidad de la clase Jugador, implementando los siguientes métodos:
• golpeado: quita vida al jugador.
• golpear: quita vida al enemigo y lo agrega a la lista de enemigos golpeados. 
"""

class Entidad:

  def __init__(self, vida_inicial: int):
    self.vida = vida_inicial

class Enemigo(Entidad):
  pass

class Jugador(Entidad):

  def __init__(self, vida_inicial: int):
    super().__init__(vida_inicial)
    self.enemigos_golpeados = []

  def golpeado(self, cuanto: float):
    self.vida -= cuanto
    

  def golpear(self, enemigo: 'Enemigo', cuanto: float):
    enemigo.vida -= cuanto
    self.enemigos_golpeados.append(enemigo)
    
""" enemigo = Enemigo(100)

jugador = Jugador(100)

print(f"Enemigo: {enemigo.vida}")

print(f"jugador: {jugador.vida}")

jugador.golpear(enemigo, 20)


print(f"Enemigo: {enemigo.vida}")

print(f"jugador: {jugador.vida}")
print(f"jugador: {jugador.enemigos_golpeados}") """
