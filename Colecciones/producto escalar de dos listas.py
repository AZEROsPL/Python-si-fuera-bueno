lista1 = [int(x) for x in input("Lista A : ").split()]
lista2 = [int(x) for x in input("Lista B : ").split()]
producto_escalar = sum(a * b for a, b in zip(lista1, lista2))
print("Producto escalar =", producto_escalar)