lista = [int(x) for x in input("Ingrese una lista de números: ").split()]
promedio = sum(lista) / len(lista)
mayores = [x for x in lista if x > promedio]
print("Promedio:", promedio)
print("Mayores que el promedio:", mayores)