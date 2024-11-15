def buscar_elemento_en_lista():
    """
    Busca elementos en una lista de numeros 
    Maneja las excepciones ValueError y limita los intentos fallidos a 3.
    """

    numeros = []
    while True:
        numero = int(input("Ingrese un numero entero (o -1 para terminar): "))
        if numero == -1:
            break
        numeros.append(numero)

    errores = 0
    while errores < 3:
        buscar = int(input("Ingrese el numero a buscar: "))
        try:
            indice = numeros.index(buscar)
            print(f"El numero {buscar} se encuentra en la posicion {indice}")
        except ValueError:
            print("El numero no se encuentra en la lista.")
            errores += 1
            if errores == 3:
                print("Demasiados intentos fallidos. Finalizando el programa.")

if __name__ == "__main__":
    buscar_elemento_en_lista()