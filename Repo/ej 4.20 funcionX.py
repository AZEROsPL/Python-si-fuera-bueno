valx = int(input("Ingrese el máximo valor para x: "))
if valx < 0:
    while valx < 0:
        valx = int(input("Ingrese un valor valido maximo para x: "))
for x in range (0, valx+1, 2):
    func = x**3 + x**2 -5
    print ("Para x = ", x, " f(x) = ", func)