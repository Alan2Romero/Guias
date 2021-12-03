ejecutar = "ejecutar"
def main():
    lista = []
    numero = 1
    cantidad = 0
    while numero > 0:
        numero = float(input("Ingrese un valor positivo(Valor negativo si quiere terminar):"))
        if numero < 0:
            operacion(lista,cantidad)
        else:
            cantidad += 1
            lista.append(numero)
def operacion(lista,cantidad):
    suma_total = sum(lista)
    suma_prom = suma_total // cantidad
    print(f"Los valores ingresados son:{lista}. La suma total es {suma_total} Y el promedio es {suma_prom}")
    
    
    
if ejecutar == "ejecutar":
    main()
