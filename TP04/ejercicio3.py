def separar_claves(clave_maestra):

  clave1 = ""
  clave2 = ""
  for i, digito in enumerate(str(clave_maestra)):
      if i % 2 == 0:
          clave1 += digito
      else:
          clave2 += digito
  return int(clave1), int(clave2)


clave_maestra = int(input("ingrese la clave maestra: "))
clave1, clave2 = separar_claves(clave_maestra)
print("Clave 1:", clave1)
print("Clave 2:", clave2)