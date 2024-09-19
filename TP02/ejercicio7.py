import random
def intercalar_listas(lista1, lista2):
  
  i = 0
  for elemento in lista2:
    lista1.insert(2*i, elemento)
    i += 1


lista1 = [random.randint(1, 10) for _ in range(5)]
lista2 = [random.randint(1, 10) for _ in range(5)]
print("Lista 1:", lista1)
print("Lista 2:", lista2)
intercalar_listas(lista1, lista2)
print("Lista 1 después de intercalar:", lista1)