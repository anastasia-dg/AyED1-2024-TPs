def crear_matriz(n):
  matriz = []
  for i in range(n):
    fila = []
    for j in range(n):
      valor = int(input(f"Ingrese el valor para la posición [{i},{j}]: "))
      fila.append(valor)
    matriz.append(fila)
  return matriz

def imprimir_matriz(matriz):
  for fila in matriz:
    print(fila)

def ordenar_filas(matriz):
  for fila in matriz:
    fila.sort()

def intercambiar_filas(matriz, fila1, fila2):
  matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def intercambiar_columnas(matriz, col1, col2):
  for i in range(len(matriz)):
    matriz[i][col1], matriz[i][col2] = matriz[i][col2], matriz[i][col1]

def transponer_matriz(matriz):
  for i in range(len(matriz)):
    for j in range(i+1, len(matriz)):
      matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

def promedio_fila(matriz, fila):
  suma = sum(matriz[fila])
  promedio = suma / len(matriz[fila])
  return promedio

def porcentaje_impares_columna(matriz, columna):
  cont_impares = 0
  for fila in matriz:
    if fila[columna] % 2 != 0:
      cont_impares += 1
  porcentaje = (cont_impares / len(matriz)) * 100
  return porcentaje

def es_simetrica_principal(matriz):
  n = len(matriz)
  for i in range(n):
    for j in range(i+1, n):
      if matriz[i][j] != matriz[j][i]:
        return False
  return True

def es_simetrica_secundaria(matriz):
  n = len(matriz)
  for i in range(n):
    for j in range(n-i-1):
      if matriz[i][j] != matriz[n-j-1][n-i-1]:
        return False
  return True

def columnas_palindromos(matriz):
  palindromos = []
  for j in range(len(matriz)):
    columna = [fila[j] for fila in matriz]
    if columna == columna[::-1]:
      palindromos.append(j)
  return palindromos

if __name__ == "__main__":
  n = int(input("Ingrese el tamaño de la matriz: "))
  matriz = crear_matriz(n)

  print("Matriz original:")
  imprimir_matriz(matriz)

  
  ordenar_filas(matriz)
  print("\nMatriz con filas ordenadas:")
  imprimir_matriz(matriz)

  
  intercambiar_filas(matriz, 0, 1)
  print("\nMatriz con filas 0 y 1 intercambiadas:")
  imprimir_matriz(matriz)

  intercambiar_columnas(matriz, 0, 1)
  print("\nMatriz con columnas 0 y 1 intercambiadas:")
  imprimir_matriz(matriz)

  promedio_fila1 = promedio_fila(matriz, 0)
  print(f"Promedio de la primera fila: {promedio_fila1}")

  porcentaje = porcentaje_impares_columna(matriz, 0)
  print(f"el porcentaje  es: {porcentaje}")

  palindromos = columnas_palindromos(matriz)
  print(f"las columnas palindromos son: {palindromos}")
  
  if es_simetrica_principal(matriz):
    print("La matriz es simétrica respecto a la diagonal principal")
  else:
    print("La matriz no es simétrica respecto a la diagonal principal")
  if es_simetrica_secundaria(matriz):
    print("La matriz es simetrica respecto a la diagonal secundaria")
  else:
    print("La matriz no es simetrica respecto a la diagonal secundaria")
