total = 0
cantidad = 0
for i in range(3):
    nombres, notas = input("Ingrese nombre y notas (ej: Juan:5,4,3): ").split(":")
    # Convertir las notas a números
    conjunto = []
    for nota in notas.split(","):
        conjunto.append(float(nota))
    # Acumular el total
    total += sum(conjunto)
    cantidad += len(conjunto)
promedio_general = total / cantidad
print("Promedio general:", promedio_general)