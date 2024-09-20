palos = ["Oro", "Copa", "Espada", "Basto"]
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

baraja = [f"{numero} {palo}" for numero in numeros for palo in palos]

print(baraja)