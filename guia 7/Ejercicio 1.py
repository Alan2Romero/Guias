ejecutar = "ejecutar"
def main():
    eleccion=int(input("""
    1- Validar si el año es bisiesto
    2- Devolver cantidad de dias correspondientes dado un mes y un año
    3- Validar fecha
    4- Dada una fecha indicar los dias que faltan hasta fin de mes
    5- Dada una fecha indicar los dias que faltan hasta fin de año
    6- Dada una fecha indicar la cantidad de dias transcurridos en ese año hasta esa fecha
    7- Dada dos fechas indicar el tiempo entre ambas.
    8- Salir
    """))
    if eleccion == 1:
        año_bisiesto()
    elif eleccion == 2:
        dias_correspondientes()
    elif eleccion == 3:
        validacion()
    elif eleccion == 4:
        opcion = 1
        dias_faltantes(opcion)
    elif eleccion == 5:
        opcion = 2
        dias_faltantes(opcion)
    elif eleccion == 6:
        dias_transcurridos()
    elif eleccion == 7:
        tiempo_entre()
    elif eleccion == 8:
        print("Hasta nuevo")

def año_bisiesto():
    año = int(input("Inserte un año"))
    resultado = año // 4
    resultado2 = año // 400
    if resultado == 0 or resultado2 == 0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
    main()
def dias_correspondientes():
    meses =["","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    año = int(input("Inserte un año"))
    mes = int(input("Inserte un mes(Formato numero)"))
    añob = año // 4
    añob2 = año // 400
    mes_real = meses[mes]
    if añob == 0 or añob2 == 0:
        if mes == 2:
            print(f"{mes_real} tiene 29 dias")
    else:
        if mes == 2:
            print(f"{mes_real} tiene 28 dias")
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            print(f"{mes_real} tiene 31 dias")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print(f"{mes_real} tiene 30 dias")
    main()
def validacion():
    año = int(input("Inserte un año"))
    mes = int(input("Inserte un mes(Formato numero)"))
    dia = int(input("Inserte un dia(Formato numero"))
    if año < 0:
        print("Inserte un año valido")
        main()
    else:
        if mes < 0 or mes > 12:
            print("Inserte un mes valido")
            main()
        else:
            if dia < 0:
                print("Inserte un dia valido")
            else:
                if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                    if dia > 31:
                        print("Inserte un dia valido")
                
                elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    if dia > 30:
                        print("Inserte un dia valido")
    main()
def dias_faltantes(opcion):
    año = int(input("Inserte un año"))
    mes = int(input("Inserte un mes(Formato numero)"))
    dia = int(input("Inserte un dia(Formato numero)"))
    añob = año // 4
    añob2 = año // 400
    resultado = 0
    i=0
    if opcion == 1:
        if añob == 0 or añob2 == 0:
            if mes == 2:
                año = 366
                resultado = 29 - dia
                print(f"Faltan {resultado} dias para fin de mes")
        else:
            if mes == 2:
                año = 365
                resultado = 28 - dia
                print(f"Faltan {resultado} dias para fin de mes")
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            resultado = 31 - dia
            print(f"Faltan {resultado} dias para fin de mes")
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            resultado = 30 - dia
            print(f"Faltan {resultado} dias para fin de mes")
    if opcion == 2:
        for _ in range(0,mes):
            i+=1
            if añob == 0 or añob2 == 0:
                if i == 2:
                    año = 366
                    resultado += 29
            else:
                if i == 2:
                    año = 365
                    resultado += 28
                else:
                    año = 365
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                resultado += 31
            elif i == 4 or i == 6 or i == 9 or i == 11:
                resultado += 30
        resultado = resultado - (dia + año) * -1
        print(f"Faltan {resultado} dias para fin de año")
    main()
def dias_transcurridos():
    año = int(input("Inserte un año"))
    mes = int(input("Inserte un mes(Formato numero)"))
    dia = int(input("Inserte un dia(Formato numero)"))
    añob = año // 4
    añob2 = año // 400
    resultado = 0
    i=0
    for _ in range(0,mes):
        i+=1
        if añob == 0 or añob2 == 0:
            if i == 2:
                resultado += 29
        else:
            if i == 2:
                resultado += 28
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            resultado += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            resultado += 30
    resultado = resultado - dia
    print(f"Transcurrieron {resultado} dias hasta la fecha")    
def tiempo_entre():
    año1 = int(input("Inserte un año"))
    mes1 = int(input("Inserte un mes(Formato numero)"))
    dia1 = int(input("Inserte un dia(Formato numero)"))
    print("Inserte fecha que quiere saber cuanto tiempo transcurrio")
    año2 = int(input("Inserte el segundo año"))
    mes2 = int(input("Inserte el segundo mes(Formato numero)"))
    dia2 = int(input("Inserte el segundo dia(Formato numero)"))
    resultado = 0
    añob = año1 // 4
    añob2 = año1 // 400
    año_total = año2 - año1
    mes_total = mes2 - mes1
    while mes_total < 0:
        año_total -=1
        mes_total +=12
    dia_total = dia2 - dia1
    while dia_total < 0:
        mes_total -=1
        if añob == 0 or añob2 == 0:
            if mes == 2:
                resultado += 29
        else:
            if mes == 2:
                resultado += 28
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            resultado += 31
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            resultado += 30
    print(f"El tiempo transcurrido fue de: {año_total} años, {mes_total} meses Y {dia_total} dias.")
    main()

if ejecutar == "ejecutar":
    main()
    ejecutar = "w"
