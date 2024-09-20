import random

def generar_matriz_aleatoria(n):
  numeros = list(range(n * n))  
  random.shuffle(numeros)  

  matriz = []
  for i in range(n):
    fila = numeros[i*n: (i+1)*n]
    matriz.append(fila)

  return matriz

if __name__ == "__main__":
  n = int(input("Ingrese el tamaño de la matriz (N): "))
  matriz = generar_matriz_aleatoria(n)

  print("Matriz generada:")
  for fila in matriz:
    print(fila)