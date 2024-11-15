def nombre_mes(numero_mes):
  """
  Devuelve el nombre del mes correspondiente a un numero

  Args: un numero entero que representa el mes (1-12)

  Returns: una cadena con el nombre del mes, o una cadena vacia si el numero es invalido.
  """

  meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
           "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

  try:
    if not 1 <= numero_mes <= 12:
      raise ValueError("Numero de mes invalido")

    return meses[numero_mes - 1]
  except ValueError as e:
    print(f"Error: {e}")
    return ""


print(nombre_mes(3))  
print(nombre_mes(15))