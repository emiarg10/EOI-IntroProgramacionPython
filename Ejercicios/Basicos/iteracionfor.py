contadornumero = 0

for numero in range (1,21,2):
    contadornumero+=1

    if (contadornumero<=5):
        continue # Salta a la linea del for
    
    print(numero)
print("Numero de la serie",contadornumero)
    
