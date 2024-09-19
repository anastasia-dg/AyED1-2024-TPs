import random

def esta_ordenada(lista):
  for i in range(len(lista) - 1):
    if lista[i] > lista[i+1]:
      return False
  return True


lista_aleatoria = [random.randint(1, 10) for _ in range(10)]
print("Lista aleatoria:", lista_aleatoria)
print("¿Está ordenada?", esta_ordenada(lista_aleatoria))