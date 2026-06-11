total = 0
while True:
    print("Ingrese la primera nota:")
    nota1 = float(input())
    print("Ingrese la segunda nota:")
    nota2 = float(input())
    print("Ingrese la tercera nota:")
    nota3 = float(input())
    print("Ingrese la cuarta nota:")
    nota4 = float(input())
    print("Ingrese la quinta nota:")
    nota5 = float(input())
    total = nota1 + nota2 + nota3 + nota4 + nota5
    if total > 3.5 and total <= 5:
        print("Su nota es: ", str(total), " Pasa el curso")
    elif total >= 0 and total <= 3.5:
        print("Su nota es: ", str(total), " No pasa el curso")
    else:
        print("Cantidad no valida")
        print("Ingrese valores validos entre 0 y 5 con total menor a 5")
    if total <= 5 and total >= 0:
        break