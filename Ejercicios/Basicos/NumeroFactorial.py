n = input("Ingrese un numero: ")
f = 1

if (n.isdigit()):
    n=int(n)
    while n>1:
        f=f*n
        print (f"{n} {f}")
        n-=1
    print("el factorial es: ",f)
else:
    print("Introduzca un numero correcto")