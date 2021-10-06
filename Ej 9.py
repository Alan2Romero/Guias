ejecutar="ejecutar"
def main():
    hora,minuto,seg = input("Inserte una hora HH|MM|SS:").split()
    if int(seg) < 0 or int(seg) > 60:
        main()
    elif int(hora) < 0 or int(hora) > 24:
        main()
    elif int(minuto) < 0 or int(minuto) > 60:
        main()
    else:
        hora2,minuto2,seg2 = input("Inserte una hora HH|MM|SS:").split()
        if int(seg) < 0 or int(seg) > 60:
            main()
        elif int(hora) < 0 or int(hora) > 24:
            main()
        elif int(minuto) < 0 or int(minuto) > 60:
            main()
        else:
            contador_dia=0
            hora=int(hora)+int(hora2)
            minuto=int(minuto)+int(minuto2)
            seg=int(seg)+int(seg2)
            operacion(int(hora), int(minuto), int(seg), int(contador_dia))
            
def operacion(hora, minuto, seg,contador_dia):
    
    if seg > 60:
        seg-=60
        minuto+=1
        operacion(hora, minuto, segcontador_dia)
    elif minuto > 60:
        minuto-=60
        hora+=1
        operacion(hora, minuto, segcontador_dia)
    elif hora > 24:
        hora-=24
        contador_dia+=1
        operacion(hora, minuto, segcontador_dia)
    else:
        print(f"La hora nueva es:{hora}|{minuto}|{seg} Y los dias pasados fueron {contador_dia}")

if ejecutar == "ejecutar":
    main()
