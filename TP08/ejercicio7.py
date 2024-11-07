def eliminar_elementos():
    """
    Crea un conjunto de numeros del 0 al 9 y permite al usuario eliminar elementos.
    """
    conjunto_numeros = set(range(10))
    print("Conjunto inicial:", conjunto_numeros)

    while True:
        try:
            numero_a_eliminar = int(input("Ingrese un numero a eliminar (o -1 para salir): "))

            if numero_a_eliminar == -1:
                break

            conjunto_numeros.remove(numero_a_eliminar)
            print("Conjunto actualizado:", conjunto_numeros)

        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero entero.")
        except KeyError:
            print("El numero no esta en el conjunto.")


eliminar_elementos()