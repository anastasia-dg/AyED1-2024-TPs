def eliminar_subcadena_rebanadas(cadena, inicio, longitud):
    
    
    if 0 <= inicio < len(cadena) and 0 <= longitud <= len(cadena) - inicio:
        return cadena[:inicio] + cadena[inicio+longitud:]
    else:
        return "Error: Índices fuera de rango."

def eliminar_subcadena_sin_rebanadas(cadena, inicio, longitud):
    

   
    if 0 <= inicio < len(cadena) and 0 <= longitud <= len(cadena) - inicio:
        nueva_cadena = ""
        for i in range(len(cadena)):
            if i < inicio or i >= inicio + longitud:
                nueva_cadena += cadena[i]
        return nueva_cadena
    else:
        return "Error: Índices fuera de rango."

def main():
    cadena = input("Ingrese la cadena: ")
    inicio = int(input("Ingrese el índice de inicio de la subcadena a eliminar: "))
    longitud = int(input("Ingrese la longitud de la subcadena a eliminar: "))

    resultado_rebanadas = eliminar_subcadena_rebanadas(cadena, inicio, longitud)
    resultado_sin_rebanadas = eliminar_subcadena_sin_rebanadas(cadena, inicio, longitud)

    print("Utilizando rebanadas:", resultado_rebanadas)
    print("Sin utilizar rebanadas:", resultado_sin_rebanadas)

if __name__ == "__main__":
    main()