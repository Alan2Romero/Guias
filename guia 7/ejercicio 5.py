import random

def matriz(camino):
    for i in camino:
        print(i)
        
camino = []
filas = 5
columnas = 5

for i in  range(filas):
    camino.append([0]*columnas)

for f in range(filas):
    for c in range(columnas):
        camino [c][f] = random.choice(["Negro", "Rojo"])
        
matriz(camino)

for palabra in camino:
    for i in range(len(palabra)):
        if palabra[i] == "Rojo":
            palabra[i] = "Verde"
        
matriz(camino)
