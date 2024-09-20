def centrar_cadena(cadena, ancho_pantalla=80):

  espacios_a_la_izquierda = (ancho_pantalla - len(cadena)) // 2
  return " " * espacios_a_la_izquierda + cadena


cadena = input("Ingrese la cadena a centrar: ")


cadena_centrada = centrar_cadena(cadena)
print(cadena_centrada)