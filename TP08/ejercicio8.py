def generar_diccionario_cuadrados():
  """
  funcion: genera un diccionario donde las claves son numeros del 1 al 20 y los valores son sus cuadrados.

  """

  diccionario_cuadrados = {}
  for numero in range(1, 21):
    diccionario_cuadrados[numero] = numero ** 2
  return diccionario_cuadrados

resultado = generar_diccionario_cuadrados()

print(resultado)