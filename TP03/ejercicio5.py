import random

def cargar_sala(sala, porcentaje_ocupacion):
    
    num_filas, num_columnas = len(sala), len(sala[0])
    total_butacas = num_filas * num_columnas
    butacas_a_ocupar = int(total_butacas * porcentaje_ocupacion / 100)

    for _ in range(butacas_a_ocupar):
        fila = random.randint(0, num_filas - 1)
        columna = random.randint(0, num_columnas - 1)
        while sala[fila][columna] == 1:  
            fila = random.randint(0, num_filas - 1)
            columna = random.randint(0, num_columnas - 1)
        sala[fila][columna] = 1

def mostrar_butacas(sala):
    
    for fila in sala:
        print(' '.join(['O' if butaca else 'L' for butaca in fila]))

def reservar_butaca(sala, fila, columna):
   
    if 0 <= fila < len(sala) and 0 <= columna < len(sala[0]) and sala[fila][columna] == 0:
        sala[fila][columna] = 1
        return True
    return False

def butacas_libres(sala):
   
    return sum(sum(fila) for fila in sala)

def butacas_contiguas(sala):
 
    max_secuencia = 0
    inicio_max = 0
    for i, fila in enumerate(sala):
        contador = 0
        inicio = 0
        for j, butaca in enumerate(fila):
            if butaca == 0:
                contador += 1
            else:
                if contador > max_secuencia:
                    max_secuencia = contador
                    inicio_max = inicio
                contador = 0
                inicio = j + 1
        if contador > max_secuencia:
            max_secuencia = contador
            inicio_max = inicio
    return i, inicio_max, inicio_max + max_secuencia

num_filas = 10
num_columnas = 15
porcentaje_ocupacion = 50

sala = [[0 for _ in range(num_columnas)] for _ in range(num_filas)]
cargar_sala(sala, porcentaje_ocupacion)

mostrar_butacas(sala)


fila_a_reservar = 3
columna_a_reservar = 5
if reservar_butaca(sala, fila_a_reservar, columna_a_reservar):
    print("Butaca reservada con éxito.")
else:
    print("La butaca no está disponible.")

mostrar_butacas(sala)


print("Butacas libres:", butacas_libres(sala))


fila, inicio, fin = butacas_contiguas(sala)
print("Secuencia más larga de butacas libres en la fila", fila, "desde", inicio, "hasta", fin - 1)