def es_fecha_valida(fecha):

  año, mes, dia = fecha
  dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if mes < 1 or mes > 12 or dia < 1 or dia > dias_en_mes[mes-1]:
    return False
  
  if mes == 2 and dia == 29:
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)
  return True

def sumar_dias(fecha, dias):
  
  año, mes, dia = fecha
  dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  while dias > 0:
    dia += 1
    if dia > dias_en_mes[mes-1]:
      dia = 1
      mes += 1
      if mes > 12:
        mes = 1
        año += 1
        
        dias_en_mes[1] = 29 if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0) else 28
    dias -= 1

  return año, mes, dia

def es_horario_valido(horario):
 
  hora, minuto = horario
  return 0 <= hora <= 23 and 0 <= minuto <= 59

def diferencia_horarios(horario1, horario2):
  
  hora1, minuto1 = horario1
  hora2, minuto2 = horario2
  minutos1 = hora1 * 60 + minuto1
  minutos2 = hora2 * 60 + minuto2
  diferencia = minutos1 - minutos2
  if diferencia < 0:
    diferencia += 24 * 60
  return diferencia

def main():
  fecha_str = input("Ingrese una fecha (A-M-D): ")
  fecha = tuple(map(int, fecha_str.split('-')))
  if not es_fecha_valida(fecha):
    print("Fecha inválida.")
    return

  dias = int(input("Ingrese la cantidad de días a sumar: "))
  nueva_fecha = sumar_dias(fecha, dias)
  print("Nueva fecha:", nueva_fecha)

  horario1_str = input("Ingrese el primer horario (H:M): ")
  horario1 = tuple(map(int, horario1_str.split(':')))
  horario2_str = input("Ingrese el segundo horario (H:M): ")
  horario2 = tuple(map(int, horario2_str.split(':')))

  if not es_horario_valido(horario1) or not es_horario_valido(horario2):
    print("Horario inválido.")
    return

  
  diferencia = diferencia_horarios(horario1, horario2)
  print("Diferencia entre horarios:", diferencia, "minutos")

if __name__ == "__main__":
  main()