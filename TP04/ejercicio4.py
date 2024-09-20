def entero_a_romano(numero):

    valores_romanos = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    resultado = ''
    for valor, romano in valores_romanos:
        while numero >= valor:
            resultado += romano
            numero -= valor
    return resultado


numero = int(input("Ingrese un número entero entre 1 y 3999: "))
numero_romano = entero_a_romano(numero)
print(f"El número romano equivalente es: {numero_romano}")