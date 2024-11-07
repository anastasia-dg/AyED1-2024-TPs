def encajan_fichas(ficha1, ficha2):

  conjunto1 = set(ficha1)
  conjunto2 = set(ficha2)


  return len(conjunto1.intersection(conjunto2)) >= 1


ficha_a = (3, 4)
ficha_b = (5, 4)
ficha_c = (2, 1)

print(encajan_fichas(ficha_a, ficha_b))  
print(encajan_fichas(ficha_a, ficha_c))  