agenda = {}
while True:
    data = input("Ingrese (nombre - telefono): ")
    if data == "fin" or data == "FIN" or data == "Fin":
        break
    if "-" not in data:
        print("Formato inválido. Use: Nombre - Número")
        continue
    nombre, numero = map(str.strip, data.split("-", 1))
    if not nombre or not numero:
        print("Debe ingresar un nombre y un número separados por '-' correctamente.")
        continue
    agenda[nombre] = numero
print(agenda)
