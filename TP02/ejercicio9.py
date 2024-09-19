A = int(input("Ingrese el valor inicial: "))
B = int(input("Ingrese el valor final: "))
lista_multiplos = [num for num in range(A, B+1) if num % 7 == 0 and num % 5 != 0]
print(lista_multiplos)