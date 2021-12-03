## 1 es negro
## 0 es blanco
import random
nota_piano = []
nota_esperada = []
for _ in range(0,88):
    a = random.randint(0,1)
    nota_piano.append(a)
for _ in range(0,88):
    b = random.randint(0,1)
    nota_esperada.append(b)
nota_afinada = []
ejecutar = "ejecutar"
def VerificarAfinacionDePiano():
    for i in range(0,88):
        nota = nota_piano[i]
        esperada = nota_esperada[i]
        if nota != esperada:
            nota_afinada.append("Rojo")
        else:
            nota_afinada.append("")
        nota = ""
        esperada = ""
    print(nota_afinada)

if ejecutar == "ejecutar":
    VerificarAfinacionDePiano()
            
