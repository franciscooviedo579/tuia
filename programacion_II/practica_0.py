# Practica 0 - Recursion - Programacion II - TUIA

# Ejercicio 0

def factorial(n: int) -> int:
  if(n == 0): return 1

  return n * factorial(n - 1)

numero = 5
resultado = factorial(numero) # resultado 120

print("El resultado de factorial de " + str(numero) + " es " + str(resultado))