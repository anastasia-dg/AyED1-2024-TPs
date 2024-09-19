import random
def normalizar_lista(lista):
 
  suma_total = sum(lista)
  for i in range(len(lista)):
    lista[i] /= suma_total


lista_aleatoria = [random.randint(1, 10) for _ in range(5)]
print("Lista original:", lista_aleatoria)
normalizar_lista(lista_aleatoria)
print("Lista normalizada:", lista_aleatoria)