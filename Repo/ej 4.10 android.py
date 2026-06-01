voto = "si"
android = 0
ios = 0
while voto == "si" or voto == "Si" or voto == "SI":
    voto = str(input("Votar por Android?: "))
    if voto == "si" or voto == "Si" and voto == "SI":
        android = android + 1
        print ("Se ha seleccionado: Android")
    else:
        voto = str(input("Votar por IOS?: "))
        if voto == "si" or voto == "Si" and voto == "SI":
            ios = ios + 1
            print ("Se ha seleccionado: IOS")
        else:
            print("Voto No valido")
    print ("Votos Android: ", android)
    print ("Votos IOS: ", ios)
    voto = str(input("Añadir mas votos?:"))
if android > ios:
    print("Android es ganador de la votación")
elif ios > android:
    print("IOS es ganador de la votación")
else:
    print("Empate en la votación")