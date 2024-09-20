def es_capicua(cadena):
 
  izquierda = 0
  derecha = len(cadena) - 1

  while izquierda < derecha:
    if cadena[izquierda] != cadena[derecha]:
      return False
    izquierda += 1
    derecha -= 1

  return True

# bloque principal
cadena = input("Ingrese una cadena: ")
if es_capicua(cadena):
  print(cadena, "es capicúa.")
else:
  print(cadena, "no es capicúa.")