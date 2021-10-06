ejecutar="ejecutar"
def main():
    año,mes,dia = input("Inserte una fecha AAAA|MM|DD:").split()
    if int(dia) < 0 or int(dia) > 31:
        main()
    elif int(año) < 0:
        main()
    elif int(mes) < 0 or int(mes) > 12:
        main()
    else:
        dias = int(input("Inserte cantidad de dias"))
        dia=int(dia)+dias
        operacion(int(año), int(mes), int(dia), int(dias))
        

def operacion(año, mes, dia, dias):
    if dia > 31:
        dia-=31
        mes+=1
        if mes > 12:
            mes = 1
            año+=1
        operacion(año, mes, dia, dias)
    else:
        print(f"{año}|{mes}|{dia}")

if ejecutar == "ejecutar":
    main()



















