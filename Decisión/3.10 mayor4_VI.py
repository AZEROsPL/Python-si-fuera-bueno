print("Ingrese el primer número:")
a = float(input())
print("Ingrese el segundo número:")
b = float(input())
print("Ingrese el tercer número:")
c = float(input())
print("Ingrese el cuarto número:")
d = float(input())
if a > b:
    if a > c:
        if a > d:
            print("El número mayor es:", a)
        else:
            print("El número mayor es:", d)
    elif c > d:
        print("El número mayor es:", c)
    else:
        print("El número mayor es:", d)
elif b > c:
    if b > d:
        print("El número mayor es:", b)
    else:
        print("El número mayor es:", d)
elif c > d:
    print("El número mayor es:", c)
else:
    print("El número mayor es:", d)