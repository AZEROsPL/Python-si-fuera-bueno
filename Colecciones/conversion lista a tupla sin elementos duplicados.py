lista = eval(input("Ingrese una lista de elementos: "))
tupla = tuple(set(lista))
print("La tupla sin duplicados es:", tupla)