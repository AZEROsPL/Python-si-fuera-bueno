a = float(input("Ingrese el valor minimo:"))
b = float(input("Ingrese el valor maximo:"))
c = float(input("Ingrese un número averiguar si se encuentra en el intervalo [{},{}]: ".format(a, b)))
if c >= a and c <= b:
    print("El número insertado se encuentra en el intervalo [{},{}]: ".format(a, b))
else:
    print("El número insertado no se encuentra en el intervalo [{},{}]: ".format(a, b))