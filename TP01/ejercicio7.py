
def sumar_n_dias():
    
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    ano = int(input("Ingrese el año: "))
    n = int(input("Ingrese la cantidad de días a sumar: "))

  

    print(f"La nueva fecha es: {dia}/{mes}/{ano}")

def calcular_diferencia_dias():
   
    dia1 = int(input("Ingrese el día de la primera fecha: "))
    mes1 = int(input("Ingrese el mes de la primera fecha: "))
    ano1 = int(input("Ingrese el ano de la primera fecha: "))
    dia2 = int(input("Ingrese el día de la segunda fecha: "))
    mes2 = int(input("Ingrese el mes de la segunda fecha: "))
    ano2 = int(input("Ingrese el ano de la segunda fecha: ")) 

    dias = 0
   

    print(f"La diferencia en días es: {dias}")

# Menú principal
while True:
    
    print("1. Sumar N días a una fecha")
    print("2. Calcular la diferencia entre dos fechas")
    print("3. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        sumar_n_dias()
    elif opcion == 2:
        calcular_diferencia_dias()
    elif opcion == 3:
        break
    else:
        print("Opción inválida.")