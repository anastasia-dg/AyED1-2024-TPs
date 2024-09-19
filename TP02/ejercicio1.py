import random

def cargar_lista_aleatoria():
   
    cantidad = random.randint(10, 99)
    lista = [random.randint(1000, 9999) for _ in range(cantidad)]
    return lista

def calcular_producto(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

def eliminar_valor(lista, valor):
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            lista.pop(i)
        else:
            i += 1

def es_capicua(lista):
    return lista == lista[::-1]

#bloque principal
lista = cargar_lista_aleatoria()
print("Lista original:", lista)

producto = calcular_producto(lista)
print("Producto:", producto)

valor_eliminar = int(input("Ingrese el valor a eliminar: "))
eliminar_valor(lista, valor_eliminar)
print("Lista después de eliminar:", lista)

print("¿Es capicúa?", es_capicua(lista))