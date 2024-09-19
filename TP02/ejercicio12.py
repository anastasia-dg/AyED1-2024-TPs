def registrar_visitas():
   
    visitas = {}
    while True:
        socio = int(input("Ingrese el número de socio (5 dígitos, 0 para finalizar): "))
        if socio == 0:
            break
        if 10000 <= socio <= 99999:
            visitas[socio] = visitas.get(socio, 0) + 1
        else:
            print("Número de socio inválido. Debe tener 5 dígitos.")
    return visitas

def mostrar_frecuencia_visitas(visitas):
    
    print("Frecuencia de visitas por socio:")
    for socio, cantidad in visitas.items():
        print(f"Socio {socio}: {cantidad} visitas")

def eliminar_socio(visitas):
    
    socio_baja = int(input("Ingrese el número de socio a dar de baja: "))
    visitas_eliminadas = visitas.pop(socio_baja, 0)
    print(f"Se eliminaron {visitas_eliminadas} ingresos del socio {socio_baja}")

if __name__ == "__main__":
    visitas = registrar_visitas()
    mostrar_frecuencia_visitas(visitas)
    eliminar_socio(visitas)
    print("Registros actualizados:")
    mostrar_frecuencia_visitas(visitas)