tamaño_matriz = int(input("Ingrese el tamaño de la matriz identidad: "))
matriz_identidad = [[1 if i == j else 0 for j in range(tamaño_matriz)] for i in range(tamaño_matriz)]
print("Matriz Identidad:")
for a in matriz_identidad:
    print(a)