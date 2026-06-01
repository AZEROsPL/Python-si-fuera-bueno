# Un diccionario almacena pares: valor
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Bogotá"}
print(persona["nombre"])
print(persona.get("correo"))

# Agregar, eliminar y modificar elementos
persona["correo"] = "ana@example.com"
persona["edad"] = 26
print(persona)
persona.update({"pais": "Colombia"})
print(persona)

valor = persona.pop("correo", None)
ultimo = persona.popitem()
print(valor)
print(ultimo)
print(persona)

print("----------------------------------------------------------------------")

# Recorridos comunes

for clave in persona.keys():
    print("clave:", clave)
for valor in persona.values():
    print("valor:", valor)
for clave, valor in persona.items():
    print(clave, "->", valor)
    
print("----------------------------------------------------------------------")

# Otros métodos utiles
config = {"modo": "dev"}
print(config)
config.setdefault("puerto", 8000)
print(config)
persona.clear()
print(persona)