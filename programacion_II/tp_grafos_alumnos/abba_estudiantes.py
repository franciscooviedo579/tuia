from itertools import permutations, product
from collections import deque

"""
Alumnos:
  - Larrubia, Agustin.
  - Oviedo, Francisco.
  - Calenta, Nicolas.
"""

def es_palindromo(s: str) -> bool:
    """
    Determina si una cadena es un palíndromo. Una cadena es palíndromo si se lee
    igual de izquierda a derecha y de derecha a izquierda.
    """
    if(len(s) <= 1):
        return True
    if(s[0] == s[-1]):
        cadena_recortada = s[1:-1]
        return es_palindromo(cadena_recortada)
    else:
        return False

class GrafoDirigido:
    def __init__(self) -> None:
        """Inicializa un grafo dirigido vacío."""
        self.vertices = {}
    
    def agregar_vertice(self, vertice) -> None:
        """Agrega un vértice al grafo si no existe."""
        if vertice not in self.vertices:
            self.vertices[vertice] = set()
    
    def agregar_arista(self, origen, destino) -> None:
        """Agrega una arista dirigida desde `origen` hacia `destino`."""
        if origen not in self.vertices:
            self.agregar_vertice(origen)
        if destino not in self.vertices:
            self.agregar_vertice(destino)
        self.vertices[origen].add(destino)
    
    def __eq__(self, other: "GrafoDirigido") -> bool:
        """Compara dos grafos dirigidos sin importar el orden de los vértices y aristas."""
        if not isinstance(other, GrafoDirigido):
            return False
        return self.vertices == other.vertices
    
def generar_G_r(n: int, alfabeto: list[str]) -> GrafoDirigido | None:
    """
    Genera el grafo de reemplazos para todas las cadenas posibles de longitud `n`
    construidas a partir de un conjunto de caracteres (alfabeto) dado.

    En el grafo de reemplazos, los nodos representan todas las combinaciones
    posibles de caracteres de longitud `n` generadas a partir del alfabeto.
    Dos nodos `s` y `s'` están conectados mediante una arista dirigida de `s` a `s'`
    si `s'` puede obtenerse de `s` mediante una operación de reemplazo que cambia
    todas las ocurrencias de un carácter `char1` por otro carácter `char2`.

    Args:
        n (int): La longitud de las cadenas que forman los nodos del grafo.
        alfabeto (list[str]): Lista de caracteres usados para generar todas las
                              combinaciones posibles de longitud `n`.

    Returns:
        GrafoDirigido | None: El grafo de reemplazos generado. Retorna `None` si
                              `n` es 0 o si el alfabeto está vacío, ya que no
                              pueden generarse cadenas en estos casos.
    """
    # Completar 
    ...

def distancia_a_palindromo(grafo: GrafoDirigido, start: str) -> int:
    """ utiliza un algoritmo BFS para encontrar la minima distancia desde start
    a un palindromo en el grafo de reemplazos"""
    # Completar 
    ...


# Ejemplo Básico:
""" grafo = generar_G_r(4, ["o", "n", "c", "e"])
print(grafo.vecinos)
print(distancia_a_palindromo(grafo, "once")) # Deberia devolver 2. """