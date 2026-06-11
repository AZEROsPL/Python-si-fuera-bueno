dic = eval(input("Ingrese un diccionario: "))
dic_invertido = {v: k for k, v in dic.items()}
print(dic_invertido)
