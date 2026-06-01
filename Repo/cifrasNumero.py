num = int(input("Escriba un numero entero: "))

if num > 0:

    copiaNumero = num
    contadorCifras = 0
    sumaCifras = 0

    while copiaNumero > 0:

        cifra = copiaNumero % 10
        copiaNumero = copiaNumero // 10

        sumaCifras = cifra + sumaCifras
        contadorCifras = contadorCifras + 1

    print("La cantidad de cifras de:", num)
    print("son:", contadorCifras)

    print("La sumatoria es:", sumaCifras)

else:
    print("No es un numero positivo")