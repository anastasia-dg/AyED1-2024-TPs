def contar_vocales(palabra):
  """
  funcion: cuenta las vocales en una palabra y devuelve un diccionario con los resultados.

  precondicion:la palabra a analizar.

  postcondicion:un diccionario donde las claves son las vocales y los valores son su frecuencia.
  """

  vocales = 'aeiou'
  contador_vocales = {vocal: palabra.lower().count(vocal) for vocal in vocales}
  return contador_vocales

def analizar_frase(frase):
  """
  Analiza una frase y cuenta las vocales en cada palabra.
  """
  palabras = frase.split()
  for palabra in palabras:
    conteo = contar_vocales(palabra)
    print(f"La palabra '{palabra}' tiene las siguientes vocales:")
    for vocal, cantidad in conteo.items():
      if cantidad > 0:
        print(f" {vocal}: {cantidad}")

if __name__ == "__main__":
  frase = input("Ingrese una frase: ")
  analizar_frase(frase)