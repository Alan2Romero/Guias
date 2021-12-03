import random

def matriz(tablero):
    for i in tablero:
        print(i)
        
tablero = []
filas = 5
columnas = 5
o = 0
for i in  range(filas):
    tablero.append([0]*columnas)

for f in range(filas):
    for c in range(columnas):
        tablero [2][2] = "CABALLO"
        tablero [c][f] = random.choice(["RIVAL", "0"])


if tablero[4][1] == "RIVAL":
    tablero[1][4] = "CABALLO"
    o = 1
if o == 1:
    tablero [2][2] = "0"
    
print("TABLERO DE AJEDREZ") 
matriz(tablero)
