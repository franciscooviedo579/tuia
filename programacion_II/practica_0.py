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

""" result = mystery(7, 3)
print(result) """

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

# Ejercicio 6

# Escriba una función recursiva que tome un numero natural n e imprima todos los números
# desde n hasta 1.


def n_naturales(n: int) -> int | None:
  if(n > 1): 
    print(n)
    return n_naturales(n - 1)
  
  print(1)

""" n_naturales(16) """

# Ejercicio 7

# Convierta la siguiente función recursiva a una iterativa.

def recursiva(t: int, k: int) -> int:
  if t >= 100:
    return k
  else:
    return recursiva(t + k, k + 1)
  

def iterativa(t: int, k: int) -> int:
  while(t < 100):
    t += k
    k += 1
  return k

""" print(recursiva(50,5))

print(iterativa(50,5)) """

# Ejercicio 8

# Escriba una función recursiva que calcule el n-ésimo número triangular
# (el número 1 + 2 + 3 + ... + n).

def num_triangular(n: int) -> int:
  if(n == 1): return n

  return n + num_triangular(n - 1)

""" print(num_triangular(6)) """

# Ejercicio 9

# Escriba una función recursiva que reciba un número positivo n y devuelva
#  la cantidad de dígitos que tiene.

def cant_digitos(n: int) -> int | None:
  if(n < 10): return 1
  return 1 + cant_digitos(n // 10) 

""" print(cant_digitos(10)) """

# Ejercicio 10

# Escriba una función recursiva que reciba 2 enteros n y b y devuelva True
# si n es potencia de b.

def es_potencia(n: int, b: int) -> bool:
  if(n == 1): return True
  if(n < b): return False
  if(n % b != 0): return False

  return es_potencia(n // b, b)

  


#Ejemplos:
""" print(es_potencia(8, 2)) #-> True
print(es_potencia(64, 4)) #-> True
print(es_potencia(70, 10)) #-> False """


# Recursión con listas


# Ejercicio 11

# Escriba una función recursiva que encuentre el mayor elemento de una lista.


lista = [2,5,34546,6,53,3458437592,4,33,56]

def mayor_lista(lista: list[int]) -> int:
  if(len(lista) == 1): return lista[0]
  if(lista[0] > lista[len(lista) - 1]): 
    lista.pop(len(lista) - 1)
    return mayor_lista(lista)
  else:
    lista.pop(0)
    return mayor_lista(lista)

""" print(mayor_lista(lista)) """
    

# Ejercicio 12
# Convierta la siguiente función iterativa a una recursiva.

def iterativa_listas(l: list[int]) -> int:
  c = 1
  for i in l:
    c = c * i
  return c

def recursiva_listas(l: list[int]) -> int:
  if(len(l) == 1): return l[0]
  return l.pop(0) * recursiva_listas(l)

""" print(iterativa_listas([2,6,4]))
print(recursiva_listas([2,6,4])) """

# Ejercicio 13
# Escriba una función recursiva para replicar los elementos de una lista
# una cantidad n de veces.

# Ejemplo:
# replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])

def replicar(l: list, n: int) -> list:
  if(len(l) == 1): return [l[0]] * n
  return [l.pop(0)] * n + replicar(l,n)

""" print(replicar([1, 3, 3, 7], 2)) """

# Ejercicio 14

# Escriba una función que tome una lista y devuelva esa misma lista en orden inverso. 
# Realice dos versiones:
#  • reversaR que resuelva utilizando recursión.
#  • reversaI que resuelva utilizando iteración.
# Nota: No utilice la función built-in reversed en su solución, ni el método reversed.

def reversaR(lista: list) -> list:
  if(len(lista) == 1): return [lista[0]]
  return [lista[len(lista) - 1]] + reversaR(lista[:len(lista) - 1])

def reversaI(lista: list) -> list:

  nueva_lista = []
  for l in lista:
    nueva_lista.insert(0,l)
  return nueva_lista

""" print(reversaR([1,23,43,546,7643,32]))
print(reversaI([1,23,43,546,7643,32])) """

# Ejercicio 15

# Escribir una función recursiva que reciba como parámetros dos cadenas a y b, 
# y encuentre la posición de la primer ocurrencia de b como subcadena de a.

def posicion_de(a: str, b: str) -> int | None:
  if(len(a) < len(b)): return -1
  if(a.startswith(b)): return 0
  if(not a.startswith(b)): return 1 + posicion_de(a[1:],b)
  else: return 

""" print(posicion_de("Hola, Mundo","Hola")) """


# Wrappers 🌯🫔
from typing import Tuple
# Ejercicio 16

# Escriba una función recursiva que dada una cadena determine si en la misma
# hay más letras 'A' o letras 'E'. 
# Utilice una función auxiliar.

