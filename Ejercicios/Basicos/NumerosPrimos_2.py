# Numeros primos
nro = 1
numerodeprimos = input ("Numero de primos a mostrar: ")

if (numerodeprimos.isdigit()):
    numerodeprimos=int(numerodeprimos)

    while numerodeprimos > 0:
        div = 2
        band = True

        if nro == 1:
            print (f"El numero {nro} es primo")
            numerodeprimos-=1
            
        else:
            while band==True and (nro>div): #band==True equivalente a band
                if (nro%div) == 0:
                    band = False
                    break
                div+=1

            if band==True:
                print(f"El numero {nro} es primo")
                numerodeprimos-=1
        nro+=1        
else:
    print("Ingrese un numero valido")