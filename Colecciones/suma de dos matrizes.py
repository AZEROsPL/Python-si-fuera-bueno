import ast

A = ast.literal_eval(input("A = "))
B = ast.literal_eval(input("B = "))

if len(A) != len(B) or any(len(f1) != len(f2) for f1, f2 in zip(A, B)):
    print("Las matrices deben tener el mismo tamano.")
else:
    suma = [[x + y for x, y in zip(f1, f2)] for f1, f2 in zip(A, B)]
    print(suma)

