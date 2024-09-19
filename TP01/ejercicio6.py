def concatenar_numeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    num1_str = str(num1)
    num2_str = str(num2)
    
    numero_concatenado = int(num1_str + num2_str)

    return numero_concatenado

resultado = concatenar_numeros()
print("El número concatenado es:", resultado)