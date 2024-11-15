import math

def calcular_raiz_cuadrada():
  """Calcula la raiz cuadrada de un numero
  Maneja la excepcion ValueError para numeros negativos
  """

  while True:
    try:
      numero = float(input("Ingrese un numero: "))
      if numero < 0:
        raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo.")
      resultado = math.sqrt(numero)
      print("La raiz cuadrada de", numero, "es", resultado)
      break 
    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  calcular_raiz_cuadrada()