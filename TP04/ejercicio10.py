def reemplazar_palabras_iterativo(cadena, palabra_a_reemplazar, nueva_palabra):
 

  palabras = cadena.split()
  nueva_cadena = []
  num_reemplazos = 0

  for palabra in palabras:
    if palabra.lower() == palabra_a_reemplazar.lower():
      nueva_cadena.append(nueva_palabra)
      num_reemplazos += 1
    else:
      nueva_cadena.append(palabra)

  return ' '.join(nueva_cadena), num_reemplazos

cadena_original = input("ingrese la cadena a modificar: ")
palabra_a_buscar = input("ingrese la palabra a buscar: ")
nueva_palabra = input("ingrese la nueva palabra: ")

cadena_modificada, numero_reemplazos = reemplazar_palabras_iterativo(cadena_original, palabra_a_buscar, nueva_palabra)

print("Cadena modificada:", cadena_modificada)
print("Número de reemplazos:", numero_reemplazos)