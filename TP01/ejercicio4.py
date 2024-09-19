def calcular_cambio():
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))

    cambio = dinero_recibido - total_compra

    if cambio < 0:
        print("Dinero insuficiente. Por favor, ingrese un monto mayor.")
        return

    billetes = {5000: 0, 1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 10: 0}
    denominaciones = [5000, 1000, 500, 200, 100, 50, 10]

    for denominacion in denominaciones:
        while cambio >= denominacion:
            billetes[denominacion] += 1
            cambio -= denominacion

    print("El cambio es:")
    for denominacion, cantidad in billetes.items():
        if cantidad > 0:
            print(f"  {cantidad} billete/s de ${denominacion}")

calcular_cambio()