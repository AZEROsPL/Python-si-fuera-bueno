frase = str(input("Ingrese la frase: "))
palabras = frase.split()
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print(contador)