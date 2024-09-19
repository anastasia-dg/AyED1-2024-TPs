import random

def generar_lista_aleatoria(tamaño, rango_min, rango_max):
   
    return [random.randint(rango_min, rango_max) for _ in range(tamaño)]

def eliminar_elementos(lista_principal, lista_a_eliminar):
   
    for elemento in lista_a_eliminar:
        while elemento in lista_principal:
            lista_principal.remove(elemento)


tamaño_lista_principal = 10
tamaño_lista_a_eliminar = 5
rango = (1, 20)

lista_principal = generar_lista_aleatoria(tamaño_lista_principal, *rango)
lista_a_eliminar = generar_lista_aleatoria(tamaño_lista_a_eliminar, *rango)

print("Lista original:", lista_principal)
print("Elementos a eliminar:", lista_a_eliminar)

eliminar_elementos(lista_principal, lista_a_eliminar)

print("Lista resultante:", lista_principal)