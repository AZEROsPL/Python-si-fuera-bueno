num = float(input("Ingrese el número para el factorial: "))
if num < 0:
    print("No se puede calcular el factorial")
else:
    fact = 1
    inf = 1
    while inf <= num:
        fact = fact * inf
        inf = inf + 1
    print ("Factorial de ", num, " es: ", fact)