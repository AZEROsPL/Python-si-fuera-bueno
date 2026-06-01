print("Ingrese la nota definitiva:")
while True:
    nota = float(input())
    if nota < 3 and nota >= 0:
        print("Nota insuficiente")
    elif nota <= 3.5 and nota >= 0:
        print("Nota aceptable")
    elif nota <= 4.5 and nota >= 0:
        print("Nota sobresaliente")
    elif nota <= 5 and nota >= 0:
        print("Nota excelente")
    else:
        print("Nota no válida, ingrese una nota entre 0 y 5")
    if nota >= 0 and nota <= 5:
        break