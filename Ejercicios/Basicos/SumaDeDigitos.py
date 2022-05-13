nro = input("Escriba un numero: ")
resul = 0


if (nro.isdigit()):
    nro = int(nro)

    while (nro!=0):
        resul+= (nro%10)
        nro = nro//10

    print (f"El resultado es: {resul}")

else:
    print("Ingrese un numero valido")

