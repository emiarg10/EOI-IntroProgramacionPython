# A partir de un numero ingresado decir si es par o impar

nro = input("Ingrese un numero: ")
if (nro.isdigit()):
    nro=int(nro)
    
    if (nro%2==0):
        print("El numero es par")
    else:
        print("Es impar")
else:
    print("Por favor ingrese un valor numerico")

