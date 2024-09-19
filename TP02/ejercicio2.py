import random

def generar_lista_aleatoria(n):
    """Genera una lista de N números aleatorios del 1 al 100."""
    return [random.randint(1, 100) for _ in range(n)]

def tiene_repetidos(lista):
    """Determina si una lista tiene elementos repetidos."""
    return len(set(lista)) != len(lista)

def elementos_unicos(lista):
    """Devuelve una nueva lista con los elementos únicos."""
    return list(set(lista))

#bloque principal
n = int(input("Ingrese la cantidad de números: "))
lista = generar_lista_aleatoria(n)
print("Lista original:", lista)

print("¿Tiene repetidos?", tiene_repetidos(lista))
print("Elementos únicos:", elementos_unicos(lista))