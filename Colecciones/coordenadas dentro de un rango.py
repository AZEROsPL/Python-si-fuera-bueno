coordenada = eval(input("Coordenada: "))
entrada = input("Rango: ")
rango = []
numero = ""
for a in entrada:
    if a.isdigit() or a == "." or (a == "-" and numero == ""):
        numero += a
    elif numero:
        rango.append(float(numero))
        numero = ""
if numero:
    rango.append(float(numero))

n, m = rango
if n > m:
    n, m = m, n
x, y = coordenada
if n <= x <= m and n <= y <= m:
    print("Dentro del rango")
else:
    print("Fuera del rango")


