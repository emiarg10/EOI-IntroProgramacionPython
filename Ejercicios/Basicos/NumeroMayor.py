#MAYOR DE 3  

Num1=input("Introduzca el numero1: ")
Num2=input("Introduzca el numero2: ")
Num3=input("Introduzca el numero3: ")

#if(Num1.isdigit and Num2.isdigit and Num3.isdigit):

if(Num1.replace(".","",1).isdigit() and Num2.replace(".","",1).isdigit() and Num3.replace(".","",1).isdigit()):
    Num1=float(Num1) # int(num1)
    Num2=float(Num2) # int(num2)
    Num3=float(Num3) # int(num3)

    if(Num1>Num2 and Num1>Num3):
        Resul=Num1
        print("El numero mayor es : " ,Resul)

    else:

        if(Num2>Num1 and Num2>Num3):
            Resul=Num2
            print("El numero mayor es : " ,Resul)
        else:

            if (Num3>Num2 and Num3>Num1):   
                Resul=Num3
                print("El numero mayor es : " ,Resul)

            else:
                if (Num1==Num2):
                    Resul=Num1
                else:
                    Resul=Num3
                print("El numero mayor es : " ,Resul)
                #print("Hay numeros iguales")

else:

    print("Introduzca un numero valido") 