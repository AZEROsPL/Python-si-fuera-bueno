print ("Ingrese los intervalos (que no se cruzen)")
a = float(input("Ingrese el primer intervalo minimo:"))
b = float(input("Ingrese el primer intervalo maximo:"))
c = float(input("Ingrese el segundo intervalo minimo:"))
if c >= a and c <= b:
    print("Intervalo no valido (Los intervalos se cruzan)")
else:
    d = float(input("Ingrese el segundo intervalo maximo:"))
    if d >= a and d <= b:
        print("Intervalo no valido (Los intervalos se cruzan)")
    else:
        e = float(input("Ingrese el tercer intervalo minimo:"))
        if e >= a and e <= b:
            print("Intervalo no valido (Los intervalos se cruzan)")
        else:
            f = float(input("Ingrese el tercer intervalo maximo:"))
            if f >= a and f <= b or f >= c and f <= d:
                print("Intervalo no valido (Los intervalos se cruzan)")
            else:
                num = float(input("Ingrese un número para averiguar si se encuentra en alguno de los intervalos [{},{}], [{},{}], [{},{}]: ".format(a, b, c, d, e, f)))
                if num >= a and num <= b or num >= c and num <= d or num >= e and num <= f:
                    print("El número insertado se encuentra en uno de los intervalos")
                else:
                    print("El número insertado no se encuentra en uno de los intervalos")