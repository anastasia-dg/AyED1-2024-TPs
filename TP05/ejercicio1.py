def ingresar_numero():
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            if numero <= 0:
                raise ValueError("El numero debe ser mayor que 0.")
            return numero
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    try:
        numero_valido = ingresar_numero()
        print("El numero ingresado es:", numero_valido)
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")