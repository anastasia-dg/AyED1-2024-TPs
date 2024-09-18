#Un año es bisiesto si es divisible entre 4.Pero si también es divisible entre 100, no es bisiesto (excepto si es divisible entre 400).
def bisiesto(ano):
    return (ano % 4 ==  0 and ano % 100 != 0) or (ano % 400 == 0)

def fecha_valida(dia, mes, ano):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes < 1 or mes > 12:
        return False
    
    #aca si el ano es bisiesto cambio a febrero a 29 dias
    if mes == 2 and bisiesto(ano):
        dias_por_mes[1] = 29

    #aca veo que el dia ecoincida con los dias del mes q le corresponde
    if dia < 1 or dia > dias_por_mes[mes -1]:
        return False
    
    return True

dia = int(input("ingrese el dia: "))
mes = int(input("ingrese el mes: "))
ano = int(input("ingrese el ano: "))

if fecha_valida(dia, mes, ano):
    print("la fecha es valida")
else:
    print("la fecha no es valida")