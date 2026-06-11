entrada = eval(input("Ingrese una matriz para transponer: "))
transpuesta = [list(i) for i in zip(*entrada)]
print("La matriz transpuesta es:")
print(transpuesta)
print(list(zip(*entrada)))
