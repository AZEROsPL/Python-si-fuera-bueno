frase = input("Ingrese la frase: ")
palabras = frase.split()
unicas = dict.fromkeys(palabras)
print(list(unicas))