# Practica 0 - Recursion - Programacion II - TUIA

# Ejercicio 0

#  Escriba una función recursiva factorial que tome un numero natural n y calcule su factorial n!.

def factorial(n: int) -> int:
  if(n == 0): return 1

  return n * factorial(n - 1)

""" numero = 5
resultado = factorial(numero) # resultado 120

print("El resultado de factorial de " + str(numero) + " es " + str(resultado)) """

# Ejercicio 1

#  a. Escriba una función recursiva repite_hola que reciba como parámetro un número entero n y
# escriba por pantalla n veces el mensaje "Hola". Invóquela con distintos valores de n

def repite_hola(n: int) -> None:
  
  if(n > 0):
    print("Hola")
    repite_hola(n - 1)



#  b. Escriba otra función repite_hola que reciba como parámetro un número entero n y devuelva la
# cadena formada por n concatenaciones de "Hola". Invóquela con distintos valores de n

def repite_hola_v2(n: int) -> str:
  
  if(n > 1):
    return "Hola" + repite_hola_v2(n - 1)
  else:
    return "Hola"


""" repite_hola(3)

print(repite_hola_v2(2)) """

# Ejercicio 2

#  a. Escriba una función repite_saludo que reciba como parámetro un número entero n y una cadena
# saludo y escriba por pantalla n veces el valor de saludo. Invóquela con distintos valores de n y
# de saludo.

def repite_saludo(n: int, saludo: str) -> None:
  
  if(n > 0):
    print(saludo)
    repite_saludo(n - 1, saludo)


#  b. Escriba otra función repite_saludo que reciba como parámetro un número entero n y una cadena
# saludo y devuelva el valor de n concatenaciones de saludo. Invóquela con distintos valores de n
# y de saludo.


def repite_saludo_v2(n: int, saludo: str) -> str:
  
  if(n > 1):
    return saludo + repite_saludo_v2(n - 1, saludo)
  else:
    return saludo
  
""" repite_saludo(2, "Sape")

print(repite_saludo_v2(4, "Onda")) """

# Ejercicio 3

# a. Piense cuál sería el resultado de la expresión misterio(5) y luego compruebe su hipótesis
# ejecutándola.

""" El resultado seria 5, ya que suma a veces 1. """

# b. Explique con sus palabras qué hace misterio(a) para cualquier a, sea positivo, negativo o 0.

"""    
   Para numeros positivos, suma a veces 1

   Para numeros negativos da RecursionError: maximum recursion depth exceeded ya que nunca entra al caso base

   Y cuando es cero devuelve cero
"""

# Esto se puede solucionar cambiando el caso de base de == 0 a < 0

def misterio(a: int) -> int:

  if a == 0:
    return a
  
  return 1 + misterio(a - 1)

""" print(misterio(0)) """

# Ejercicio 4

def f(n: int, d: int) -> None:
  if n > 1:
    if n % d == 0:
      
      print(d)
      f(n // d, d)
    else:
      f(n, d + 1)

# 1. ¿Qué muestra por pantalla la llamada f(30, 2)? Intente deducirlo sin ejecutar el código.
 
"""     La funcion f(30,2) descompone 30 en factores primos """


""" f(18,2) """

# 2. A nivel general, ¿qué muestra por pantalla la llamada f(x, 2) para un x cualquiera?
"""     Descompone x en factores primos """


# 3. Implemente una función iterativa equivalente.

def f_v2(n: int, d: int) -> None:

  while(n > 1):
    if n % d == 0:
      print(d)
      n = n // d
    else:
      d += 1


""" f_v2(18,2) """

# Ejercicio 5

# Considere la siguiente función recursiva:
def mystery(a: int, b: int) -> int:
  if (b == 0):
    return a
  return mystery(2 * a, b - 1)

result = mystery(7, 3)
print(result)

# 1. ¿Qué muestra por pantalla este código? Intente deducirlo sin ejecutar el código.

""" La funcion mystery muestra en pantalla 56"""

# 2. ¿Cuántas veces se llama recursivamente mystery en este código?

""" Se llama a la funcion 3 veces"""

# 3. A nivel general, ¿qué muestra por pantalla la llamada f(x, 3) para un x cualquiera? 
# ¿Qué muestra por pantalla la llamada f(x, y) para x, y cualesquiera?

""" 
  Para f(x,3) muestra el resultado de hacer (2^3 * x)
  Y Para f(x,y) muestra el resultado de hacer (2^y * x)
"""

