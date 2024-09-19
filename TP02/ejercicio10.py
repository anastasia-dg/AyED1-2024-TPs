import random

lista_aleatoria = [random.randint(1, 100) for _ in range(20)]  
lista_impares = list(filter(lambda x: x % 2 != 0, lista_aleatoria))
print("Lista aleatoria:", lista_aleatoria)
print("Lista de impares:", lista_impares)