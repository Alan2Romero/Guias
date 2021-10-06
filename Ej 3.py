i = 1
Factorial = 1
numero = 1
cantidad_3 = 0
cantidad_5 = 0
cantidad_mult = 0

while numero != 0:
    numero=int(input("Introduzca un numero (Ponga 0 si no quiere continuar):"))
    ##Multiplo de 3
    if numero % 3 ==0:
        cantidad_3 += 1
    ##Multiplo de 5
    if numero % 5 ==0:
        cantidad_5 += 1
    ##Multiplo de 3 y de 5
    if numero %3 ==0 and i % 5 == 0:
        cantidad_mult += 1
    if numero < 0:
        print("No posee factorial")
    else:
        for i in range( 1, numero+1):
            Factorial = Factorial * i
        print(f"El factorial de {numero} es:{Factorial}")
        Factorial = 1
print(f"""
_________________________________________________________________
La cantidad de multiplos de 3 que hubo fue de:{cantidad_3}
La cantidad de multiplos de 5 que hubo fue de:{cantidad_5}
La cantidad de multiplos de 5 y 3 que hubo fue de:{cantidad_mult}
_________________________________________________________________
""")


    
