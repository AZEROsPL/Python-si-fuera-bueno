print("Ingrese el valor del artículo:")
valor = float(input())
print("Ingrese el tipo de artículo (1, 2, 3):")
tipo = int(input())
if tipo == 1:
    porcentaje = 0.125
elif tipo == 2:
    porcentaje = 0.083
elif tipo == 3:
    porcentaje = 0.032
else:
    porcentaje = 0
descuento = valor * porcentaje
print("El valor con descuento es:", descuento)