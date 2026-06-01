for i in range(5):
    print(i)
    break

print("---------------------------------------------------------------------")

cadena = "Python"
for letra in cadena:
    if letra == "h":
        print("se encontró la h")
        break
    print(letra)

print("---------------------------------------------------------------------")

x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
print("Fin del bucle")

print("---------------------------------------------------------------------")

for i in range(4):
    for j in range(4):
        break
    print(i, j)

print("---------------------------------------------------------------------")

cadena = "Python"
for letra in cadena:
    if letra == "P":
        continue
    print(letra)

print("---------------------------------------------------------------------")

x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)

print("---------------------------------------------------------------------")