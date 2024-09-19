def cuadrados_hasta_n(n):
   
    return [i**2 for i in range(1, n+1)]

#bloque principal
n = int(input("Ingrese el valor de N: "))
cuadrados = cuadrados_hasta_n(n)
print("Últimos 10 valores:", cuadrados[-10:])