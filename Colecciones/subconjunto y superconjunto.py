a = set(eval(input("A = ")))
b = set(eval(input("B = ")))

# Verificar subconjunto
if a.issubset(b):
    print("A es un subconjunto de B")
elif b.issubset(a):
    print("B es un subconjunto de A")
else:
    print("Ninguno es subconjunto del otro")

# Verificar superconjunto
if a.issuperset(b):
    print("A es un superconjunto de B")
elif b.issuperset(a):
    print("B es un superconjunto de A")
else:
    print("Ninguno es superconjunto del otro")