# Divisores de un numero

num=input("Ingrese un numero: ")
div = 1

if (num.isdigit()):
    num=int(num)
    while (div<=num):
        if (num%div == 0):
            print(div)
        div+=1
        
        #if (num=="N"):
         #   break
          #  print("Introduzca un numero")
