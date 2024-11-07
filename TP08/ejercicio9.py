def tabla_multiplicar(numero):
  """
  funcion: Genera la tabla de multiplicar de un numero dado.

  precondicion:el numero del cual se quiere generar la tabla de multiplicar.

 postcondicion: un diccionario con la tabla de multiplicar.
  """

  tabla = {i: numero * i for i in range(1, 13)}
  return tabla

if __name__ == "__main__":
  while True:
    try:
      N = int(input("Ingrese un numero entero (o 0 para salir): "))
      if N == 0:
        break
      resultado = tabla_multiplicar(N)
      for clave, valor in resultado.items():
        print(f"{N} x {clave} = {valor}")
    except ValueError:
      print("Entrada invalida. Por favor, ingrese un numero entero.")