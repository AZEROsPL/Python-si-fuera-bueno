tup1 = eval(input("Ingrese la primera tupla: "))
tup2 = eval(input("Ingrese la segunda tupla: "))
if tuple(tup1) == tuple(tup2):
    print("Las tuplas son iguales")
elif tuple(tup1) < tuple(tup2):
    print("La segunda tupla es mayor")
else:
    print("La primera tupla es mayor")