ejecutar = "ejecutar"
resultado = 0
def main():
    numero=int(input("Por favor ingresar el numero del dia del año:"))
    resultado = 0
    operacion(numero,resultado)
def operacion(numero,resultado):
    if numero>=0 and numero<=366:
        for i in range(numero):
            resultado+=1
            if resultado>=8:
                resultado-=8
                resultado+=1
    if resultado==1:
        print(f"El dia es lunes")
    elif resultado==2:
       print(f"El dia es martes")
    elif resultado==3:
       print(f"El dia es miercoles")
    elif resultado==4:
        print(f"El dia es jueves")
    elif resultado==5:
        print(f"El dia es viernes")
    elif resultado==6:
        print(f"El dia es sabado")
    elif resultado==7:
        print(f"El dia es domingo")
                
if ejecutar == "ejecutar":
    main()
    
