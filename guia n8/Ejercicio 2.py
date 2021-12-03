ejecutar = "ejecutar"
cantidad = 0
lista_cantidadviajes = []
lista_choferes = []
lista_chofermenorcantidad = []
lista_patentes116 = []
distancia = 0
destino = 0
patente = 0
chofer = 0
encargo = 0
finalizar = 0

def destinos():
    destino = int(input("Ingrese el numero de destino(3 digitos):"))
    cantidad = len(str(destino))
    if cantidad > 3:
        print("Ingrese un destino valido")
    else:
        distancia = int(input("Ingrese Distancia del destino en Kilometros:"))
        viajes(destino,distancia)

def viajes(destino,distancia):
    patente = int(input("Ingrese la patente del camion (6 caracteres):"))
    cantidad = len(str(patente))
    if cantidad > 6:
        print("Ingrese una patente valida")
    else:
        encargo = int(input("Ingrese el numero de destino del camion:"))
        chofer = str(input("Ingrese numero de chofer (1 a 150):"))
        choferr = int(chofer)
        if choferr > 150 or 0 > choferr:
            print("Ingrese un numero de chofer valido")
        else:
            print(destino)
            cantidad_viajes(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116)


def cantidad_viajes(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116):
    if finalizar == 1:
        lista_cantidadviajes.append(["Viajes realizados en el destino ",destino,":",cantidad])
        cantidad_km(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116)
    elif destino == encargo:
        cantidad +=1
        cantidad_km(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116)
    
def cantidad_km(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116):
    if finalizar != 1:
        lista_choferes.append([chofer,distancia])
        lista_choferes.sort()
        patentes116(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116)
    else:
        lista_chofermenorcantidad.append(lista_choferes[0])
        patentes116(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116)
        
def patentes116(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116):
    if encargo == 116:
        if finalizar != 1:
            lista_patentes116.append(patente)
            continuar(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116)
        else:
            lista_patentes116 = set(lista_patentes116)
            finalizarr()
    else:
        if finalizar != 1:
            continuar(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116)
        else:
            finalizarr()
def continuar(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116):
    continuar = int(input("""Si desea continuar agregando choferes ponga 1.
                    Si desea cambiar el destino ponga 2.
                    Si desea finalizar ponga 3.
                        """))
    if continuar == 1:
        viajes(destino,distancia)
    elif continuar == 2:
        destinos()
    elif continuar == 3:
        finalizar = 1
        cantidad_viajes(finalizar,cantidad,destino,encargo,chofer,distancia,patente,lista_patentes116)
    else:
        print("Ingrese una opcion correcta")
        
def finalizarr():
    print(f"Lista de patentes:{lista_patentes116}")
    print(f"Lista de chofer con menor cantidad de KM:{lista_chofermenorcantidad}")
    print(f"Lista de cantidad de viajes por destino: {lista_cantidadviajes}")
if ejecutar == "ejecutar":
    destinos()
                
