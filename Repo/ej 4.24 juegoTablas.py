seg = "S"
while seg == "S" or seg == "s":
    tab = int(input("Con cuál tabla desea jugar? (1, 20): "))
    while tab < 1 or tab > 20:
        tab = int(input("Inserte una tabla valida: "))
    aciertos = 0
    desaciertos = 0
    for contf in range (1, 11):
        product = tab * contf
        print ("Escriba el resultado de ", tab, " x ", contf)
        respuesta = int(input())
        if respuesta == product:
            print ("Felicitaciones!")
            aciertos = aciertos + 1
        else:
            print ("Lo siento... ese no es el resultado")
            print ("La respuesta correcta es: ", product)
            desaciertos = desaciertos + 1
    print ("Aciertos: ", aciertos)
    print ("Desaciertos: ", desaciertos)
    if aciertos <=5:
        print ("Insuficiente")
    elif aciertos <= 7:
        print ("Aceptable")
    elif aciertos <= 9:
        print ("Sobresaliente")
    else:
        print ("Excelente!")
    seg = str (input("¿Desea volver a jugar [S] o [N]?: "))
    while seg != "S" and seg != "s" and seg != "N" and seg != "n":
        seg = (input("Comando no valido, ¿Desea volver a jugar [S] o [N]?: "))