print ("Ingrese el salario base del empleado:")
salario_base = float(input())
aporte_salud = salario_base * 0.04
aporte_pension = salario_base * 0.04
descuento = aporte_salud + aporte_pension
salario_neto = salario_base - descuento
print ("El aporte a salud es de: ", str(aporte_salud))
print ("El aporte a pensión es de: ", str(aporte_pension))
print ("El descuento es de: ", str(descuento))
print ("El salario neto es a pagar es: ", str(salario_neto))