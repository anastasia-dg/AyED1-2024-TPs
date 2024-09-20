def ordenar_palabras_por_longitud(cadena):
  palabras = cadena.split()

  palabras.sort(key=len)

  
  cadena_ordenada = ' '.join(palabras)

  return cadena_ordenada


cadena_original = (input("ingrese la cadena: "))
cadena_ordenada = ordenar_palabras_por_longitud(cadena_original)
print(cadena_ordenada)  