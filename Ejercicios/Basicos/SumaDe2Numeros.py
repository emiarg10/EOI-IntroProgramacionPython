num1=input("Ingrese el numero1: ")
num2=input("Ingrese el numero2: ")

if (num1.isdigit() and num2.isdigit()):
    #num1=int(num1)
    #num2=int(num2)

    #rta = num1+num2

    #print ("El resultado es: ", rta)
    
    print (f"El resultado es: {int(num1)+int(num2)}")

else:
    print ("Ingrese un valor numerico valido")
    
