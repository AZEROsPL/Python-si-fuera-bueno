cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

contador_estudiantes = 0
aprobaron = 0
reprobaron = 0
suma_definitivas = 0

while contador_estudiantes < cantidad_estudiantes:
    codigo_estudiante = input("Ingrese el codigo del estudiante: ")
    nota_definitiva = float(input("Ingrese la nota definitiva: "))
    
    if nota_definitiva >= 3.0:
        aprobaron += 1
    else:
        reprobaron += 1

    suma_definitivas += nota_definitiva
    contador_estudiantes += 1

promedio_grupo = suma_definitivas / cantidad_estudiantes

print("La cantidad que aprobaron es:", aprobaron)
print("La cantidad que reprobaron es:", reprobaron)
print("El promedio es:", promedio_grupo)