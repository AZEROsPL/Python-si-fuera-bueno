a = float(input("Ingrese el valor del artículo a pagar: "))
descuento = input("Ingrese el tipo del artículo (textil, electrodoméstico, cocina, videojuego): ").strip().lower()

if descuento == "textil":
    precio_final = a
elif descuento in ["electrodomestico", "electrodoméstico"]:
    precio_final = a * (1 - 0.037)
elif descuento == "cocina":
    precio_final = a * (1 - 0.042)
elif descuento == "videojuego":
    precio_final = a * (1 - 0.078)
else:
    precio_final = None

if precio_final is None:
    print("El tipo de artículo no es válido. Ingrese un tipo de artículo válido.")
else:
    print("El valor a pagar es:", round(precio_final, 2))