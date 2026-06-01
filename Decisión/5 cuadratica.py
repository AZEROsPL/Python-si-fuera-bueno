print("Ingrese valores a, b, c para averiguar si la cuadratica tiene solución:")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
discriminante = b**2 - (4*a*c)
if discriminante < 0 or a == 0:
    print("La cuadratica no tiene solución")
else:
    print("La cuadratica tiene solución")