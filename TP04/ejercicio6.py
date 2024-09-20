def extraer_subcadena_rebanadas(cadena, inicio, longitud):
 

  return cadena[inicio:inicio+longitud]

def extraer_subcadena_sin_rebanadas(cadena, inicio, longitud):
  
  subcadena = ""
  for i in range(inicio, min(inicio+longitud, len(cadena))):
    subcadena += cadena[i]
  return subcadena

def main():
  cadena = input("Ingrese la cadena: ")
  inicio = int(input("Ingrese el índice de inicio: "))
  longitud = int(input("Ingrese la longitud: "))

  try:
    subcadena_rebanadas = extraer_subcadena_rebanadas(cadena, inicio, longitud)
    subcadena_sin_rebanadas = extraer_subcadena_sin_rebanadas(cadena, inicio, longitud)

    print("Utilizando rebanadas:", subcadena_rebanadas)
    print("Sin utilizar rebanadas:", subcadena_sin_rebanadas)
  except IndexError:
    print("Los índices están fuera de rango.")

if __name__ == "__main__":
  main()