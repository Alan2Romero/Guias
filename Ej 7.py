numerobase = float(input("Ingrese un valor:"))
if numerobase < 0:
    print("Ingrese un valor positivo")
else:
    exponente = int(input("Ingrese el exponente:"))
    resultado = numerobase ** exponente
    print(f"El resultado es:{resultado}")

