# Ej 1: Hola mundo

print ("Hola mundo")

# Fin Ejercicio 1


# Ej 2 : A partir de un numero ingresado diga si es mayor, menor o igual a 9

N=input("Escribir el numero: ") #N="5"

if(N.isdigit()):
    N=int(N)

    if (N==9):
        print(f"El numero: {N} es igual a 9")

    elif (int(N)>9):
        print (f"El numero: {N} es mayor a 9")
    
    else:
        print(f"El numero: {N} es menor a 9")
else:
    print("Por favor ingrese un valor numerico")

# Fin Ejercicio 2

