#
def calcular_gasto_subte(viajes, tarifa_maxima=650):
    if viajes <= 20:
        return viajes * tarifa_maxima
    elif viajes <= 30:
        return 20 * tarifa_maxima + (viajes - 20) * tarifa_maxima * 0.8
    elif viajes <= 40:
        return 20 * tarifa_maxima + 10 * tarifa_maxima * 0.8 + (viajes - 30) * tarifa_maxima * 0.7
    else:
        return 20 * tarifa_maxima + 10 * tarifa_maxima * 0.8 + 10 * tarifa_maxima * 0.7 + (viajes - 40) * tarifa_maxima * 0.6


viajes_realizados = int(input("Ingrese la cantidad de viajes realizados: "))

gasto_total = calcular_gasto_subte(viajes_realizados)

print(f"El total gastado en {viajes_realizados} viajes es: ${gasto_total:}")
