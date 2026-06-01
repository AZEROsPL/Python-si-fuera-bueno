contadorCifras = 0
sumaCifras = 0

num = int(input("Escriba el numero a analizar: "))

copiaNumero = num

while copiaNumero > 0:
    cifra = copiaNumero % 10
    copiaNumero = copiaNumero // 10
    contadorCifras = contadorCifras + 1

copiaNumero = num

while copiaNumero > 0:
    cifra = copiaNumero % 10
    copiaNumero = copiaNumero // 10
    sumaCifras = sumaCifras + cifra ** contadorCifras

if num == sumaCifras:
    print(num, "es un numero de Armstrong.")
else:
    print(num, "no es un numero de Armstrong.")