ejecutar = "ejecutar"
lista_ganadores = []
lista_ganador = []
lista_desertores = []
lista_corredores = []
trayecto = 0
tiempo = 0
numeros = 0
lotes = 0
filas = 1
columnas = 1
numero = 0
def lote(tiempo,numero,lista_ganador,lista_corredores,lotes):
    tiempo =  0
    print(f"Este es el lote {numero}")
    while tiempo != "DNF":
        numeros = str(input("Ingrese el numero del corredor:"))
        trayecto = str(input("Ingrese el numero del trayecto:"))
        tiempo = int(input("Ingrese cuanto duro el trayecto (Formato segundos) (Si abandono la carrera poner 0):"))
        if tiempo == 0 :
            tiempo = "DNF"
            lista_desertores.append([numeros,trayecto,tiempo])
        else:
            lista_corredores.append([numeros,trayecto,tiempo])
    lista_corredores.sort()
    lista_ganadores.append(lista_corredores[0])
    lista_ganador.append(lista_corredores[0])
    print(f"El ganador de la etapa {numero} es: {lista_ganador}")
    print(f"""La lista de ganadores es la siguiente:
          {lista_ganadores}""")
    print(f"""La lista de abandonos es la siguiente:
        {lista_desertores}""")
    lista_ganador = []
    lista_corredores = []

    
while lotes != 51:
    lotes+=1
    numero+=1
    lote(tiempo,numero,lista_ganador,lista_corredores,lotes)                    
                        
                
                
                
        
    
     
