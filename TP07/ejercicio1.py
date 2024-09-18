#en esta funcion busco el mayor de los 3 numeros, pensando que el primero que ingresa es el mayor
def mayor(a, b, c):
    maximo = a 
    if b > maximo:
        maximo = b
    if c > maximo: 
        maximo = c

#raca reviso si es el unico mayor
    contador = 0
    if a == maximo:
        contador += 1
    if b == maximo:
        contador += 1
    if c == maximo:
        contador += 1
    
    if contador > 1:
        return -1
    else:
        return maximo

a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
c = int(input("ingrese el tercer numero: "))

resultado = mayor(a, b ,c)
if resultado == -1:
    print("no hay un mayor")
else:
    print("es mayor es:", resultado)
    

