
import math  # Para usar la funcion sqrt()

# Definir variables
cateto1 = float(input("Introduce el primer cateto: "))
cateto2 = float(input("Introduce el segundo cateto: "))

# Calculo de la hipotenusa
hipoT = math.sqrt(cateto1**2 + cateto2**2)

# Mostrar resultado
print("La hipotenusa del triangulo es", hipoT)