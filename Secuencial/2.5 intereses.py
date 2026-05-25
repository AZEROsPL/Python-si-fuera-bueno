print ("Ingrese la cantidad de dinero:")
cantidad = float(input())
print ("Ingrese el periodo en días:")
periodo = int(input())
print ("Ingrese el porcentaje de interés:")
interes = float(input())
valor_interes = cantidad * (interes / 100 * periodo) / 365
valor_impuesto = valor_interes * 0.07
neto_a_pagar = cantidad + valor_interes - valor_impuesto
print ("Interéses ganados: ", str(valor_interes))
print ("Valor del impuesto: ", str(valor_impuesto))
print ("Total a pagar del cliente: ", str(neto_a_pagar))