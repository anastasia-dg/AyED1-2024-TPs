def eliminar_repetidos_y_ordenar(frase):
  """
  funcion:elimina las palabras repetidas de una frase y las ordena por longitud.

  precondicion:la frase de entrada.

  postcondicion:una lista con las palabras unicas ordenadas por longitud.
  """
  frase_minuscula = frase.lower()
  palabras = frase_minuscula.split()

  conjunto_palabras = set()
  for palabra in palabras:
      conjunto_palabras.add(palabra)

  lista_palabras = list(conjunto_palabras)
  lista_palabras.sort(key=len)

  return lista_palabras

frase = input("Ingrese una frase: ")
palabras_unicas = eliminar_repetidos_y_ordenar(frase)
print("Palabras unicas ordenadas por longitud:", palabras_unicas)