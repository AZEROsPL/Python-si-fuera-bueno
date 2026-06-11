while True:
    opcion = input("Ingrese el sistema operativo Android(A) o iOS(I): ")
    if opcion == "A" or opcion == "a":
        print("El sistema operativo es Android")
    elif opcion == "I" or opcion == "i":
        print("El sistema operativo es iOS")
    else:
        print("Opción no válida, ingrese A para Android o I para iOS")
    if opcion == "A" or opcion == "a" or opcion == "I" or opcion == "i":
        break