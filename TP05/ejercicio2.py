def sumar_cadenas_numericas(cadena1, cadena2):
    """
    Suma dos cadenas de caracteres 
    precondicion:  La primera cadena y la segunda cadena 

    postcondicion:
        La suma de los dos numeros
        -1 si alguna de las cadenas no es un numero valido.
    """

    try:
        numero1 = float(cadena1)
        numero2 = float(cadena2)
        return numero1 + numero2
    except ValueError:
        return -1


resultado = sumar_cadenas_numericas("3.5", "2.7")
print(resultado)

resultado = sumar_cadenas_numericas("hola", "5")
print(resultado) 