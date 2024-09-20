def ultimos_n_caracteres(cadena, n):
  if n <= 0:
    return "N debe ser un número positivo"

  
  inicio = max(0, len(cadena) - n)
  return cadena[inicio:]

if __name__ == "__main__":
  cadena = input("Ingrese la cadena: ")
  n = int(input("Ingrese el número de caracteres a extraer: "))

  resultado = ultimos_n_caracteres(cadena, n)
  print("Los últimos", n, "caracteres son:", resultado)