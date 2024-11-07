def crear_lista_precios():
  
  lista_precios = {
    "cuaderno": 1000,
    "libro": 3000,
    "lapiz": 500,
    "goma": 300,
    "boligrafo": 700
  }
  return lista_precios

def incrementar_precio_cuadernos(lista_precios):
  """
  funcion:incrementa el precio de los cuadernos.

  precondicion:el diccionario con los precios.
  postcondicion: cuadernos aumentados.
  """

  lista_precios["cuaderno"] *= 1.15

def imprimir_lista_precios(lista_precios):
  """
  funcion: imprime los elementos de la lista de precios.

  """
  for articulo, precio in lista_precios.items():
    print(f"{articulo}: ${precio}")

def encontrar_articulo_mas_caro(lista_precios):
  """
  funcion: encuentra el articulo más caro de la lista de precios.

  precondicion: el diccionario con los precios.

  postcondicion: el nombre del articulo mas caro.
  """

  articulo_mas_caro = max(lista_precios, key=lista_precios.get)
  return articulo_mas_caro


if __name__ == "__main__":
  precios = crear_lista_precios()
  incrementar_precio_cuadernos(precios)

  print("Lista de precios actualizada:")
  imprimir_lista_precios(precios)

  articulo_mas_caro = encontrar_articulo_mas_caro(precios)
  print(f"El artículo más caro es: {articulo_mas_caro}")