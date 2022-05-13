# Numeros primos

nro = input ("Ingrese un numero: ")
div = 2
band = True
if (nro.isdigit()):
    nro=int(nro)
    if nro == 1:
      print (f"El numero {nro} es primo")
    else:
        while band==True and (nro>div):
            if (nro%div) == 0:
                band = False
                break
            div+=1
        if band==True:
            print(f"El numero {nro} es primo")
        else:
            print(f"El numero {nro} NO es primo")
else:
    print("Ingrese un numero valido")