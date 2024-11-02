def fecha_extendida(fecha, año_corte=30):
  
  dia, mes, año = fecha
  meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

  if año < 100:
    año += 1900 if año > año_corte else 2000

  return f"{dia} de {meses[mes-1]} de {año}"

def main():
  fecha_str = input("Ingrese la fecha (D-M-A): ")
  dia, mes, año = map(int, fecha_str.split('-'))
  año_corte = int(input("Ingrese el año de corte: "))

  resultado = fecha_extendida((dia, mes, año), año_corte)
  print(resultado)

if __name__ == "__main__":
  main()