import random

def adivina_el_numero():
    """
    el usuario debe adivinar un numero aleatorio entre 1 y 500
    """

    numero_secreto = random.randint(1, 500)
    intentos = 0

    print("Bienvenido al juego de adivinar el numero!")
    print(" el numero es entre 1 y 500")

    while True:
        try:
            intento = int(input("Adivina el numero: "))
            intentos += 1

            if intento < numero_secreto:
                print("El numero es mayor.")
            elif intento > numero_secreto:
                print("El numero es menor.")
            else:
                print(f"¡Felicidades! adivinaste el numero en {intentos} intentos")
                break

        except ValueError:
            print("Por favor, ingresa un numero entero.")

if __name__ == "__main__":
    adivina_el_numero()