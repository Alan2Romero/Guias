Factorial = 1
numero = int(input("Ingrese un numero:"))
if numero < 0:
    print("Ingrese un valor positivo")
else:
    for i in range( 1, numero+1):
        Factorial = Factorial * i
    print(f"El factorial de {numero} es: {Factorial}")
