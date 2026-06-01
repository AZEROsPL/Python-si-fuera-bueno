frutas = ["manzana", "banana", "naranja"]
print(frutas[0])
print(frutas[-1])

frutas.append("uva")
frutas.insert(1, "pera")
print(frutas)

frutas.remove("banana")
ultimo = frutas.pop()
print("Elemento eliminado:", ultimo)
del frutas[0]
print(frutas)

print("----------------------------------------------------------------------")

numeros = [3, 7, 3, 2, 10]
print(numeros)
print(numeros.count(3))
print(numeros.index(7))
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
copia = numeros.copy()
print("copia:   ", copia)
print("numeros: ", numeros)
numeros.clear()
print(numeros)

print("----------------------------------------------------------------------")

cuadrados = [n*n for n in range(5)]
print(cuadrados)

pares = [n for n in range(10) if n % 2 == 0]
print(pares)

impares = [n for n in range(20) if n % 2 != 0]
print(impares)

print("----------------------------------------------------------------------")

