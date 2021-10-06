numerador = int(input("Ingrese el numerador de la fraccion"))
denominador = int(input("Ingrese el denominador de la fraccion"))
divisor = 2
i = 1
if denominador == 0:
    print("El denominador no puede ser 0")
else:
    while i != 0:
        ##Division
        res_num = float(numerador)/divisor
        res_den = float(denominador)/divisor

        if res_num.is_integer() and res_den.is_integer():
            print(f"{res_num}/{res_den}")
            numerador = res_num
            denominador = res_den
        else:
            if divisor == res_num or divisor == res_den or res_num <= 1 or res_den <= 1:
                print(f"La maxima expresion es:{numerador}/{denominador}")
                i = 0
            else:
                divisor +=1
               
    
                

    
    
