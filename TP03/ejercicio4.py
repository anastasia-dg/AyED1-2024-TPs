import random

def crear_matriz_produccion(num_fabricas, num_dias, capacidad_maxima):
   
    return [[random.randint(0, capacidad_maxima) for _ in range(num_dias)]
            for _ in range(num_fabricas)]

def mostrar_matriz(matriz):
   
    for fila in matriz:
        print(fila)

def calcular_produccion_total_fabricas(matriz):
   
    return [sum(fila) for fila in matriz]

def encontrar_maxima_produccion_dia_y_fabrica(matriz):
   
    max_produccion = 0
    dia_max = 0
    fabrica_max = 0
    for i, fila in enumerate(matriz):
        for j, produccion in enumerate(fila):
            if produccion > max_produccion:
                max_produccion = produccion
                dia_max = j + 1
                fabrica_max = i + 1
    return dia_max, fabrica_max, max_produccion

def calcular_produccion_total_por_dia(matriz):
    

    return [sum(col) for col in zip(*matriz)]

def encontrar_dia_mas_productivo(produccion_por_dia):
   

    return produccion_por_dia.index(max(produccion_por_dia)) + 1

def encontrar_menor_produccion_por_fabrica(matriz):
    

    return [min(fila) for fila in matriz]

# bloque principal
if __name__ == "__main__":
    num_fabricas = int(input("Ingrese el número de fábricas: "))
    capacidad_maxima = 150
    num_dias = 7

    matriz_produccion = crear_matriz_produccion(num_fabricas, num_dias, capacidad_maxima)

    print("Matriz de producción:")
    mostrar_matriz(matriz_produccion)

    produccion_total = calcular_produccion_total_fabricas(matriz_produccion)
    print("Producción total por fábrica:", produccion_total)

    dia_max, fabrica_max, max_produccion = encontrar_maxima_produccion_dia_y_fabrica(matriz_produccion)
    print(f"La fábrica {fabrica_max} produjo {max_produccion} unidades el día {dia_max}.")

    produccion_por_dia = calcular_produccion_total_por_dia(matriz_produccion)
    dia_mas_productivo = encontrar_dia_mas_productivo(produccion_por_dia)
    print(f"El día más productivo fue el día {dia_mas_productivo}.")

    menor_produccion = encontrar_menor_produccion_por_fabrica(matriz_produccion)
    print("Menor producción por fábrica:", menor_produccion)