def dia_de_la_semana(dia, mes, ano):
   
    if mes < 3:
        mes += 10
        ano -= 1
    else:
        mes -= 2
    siglo = ano // 100
    ano2 = ano % 100
    dia_semana = (((26 * mes - 2) // 10) + dia + ano2 + (ano2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if dia_semana < 0:
        dia_semana += 7
    return dia_semana

def imprimir_calendario(mes, ano):
  
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        dias_por_mes[1] = 29

    
    primer_dia = dia_de_la_semana(1, mes, ano)

   
    print(f"      Calendario: {mes}/{ano}")
    print("Do  Lu  Ma  Mi  Ju  Vi  Sa")
    print("   " * primer_dia, end="")

    for dia in range(1, dias_por_mes[mes - 1] + 1):
        print(f"{dia:2d}", end=" ")
        if (dia + primer_dia) % 7 == 0:
            print()


mes = int(input("Ingrese el mes (1-12): "))
ano = int(input("Ingrese el ano: "))

imprimir_calendario(mes, ano)