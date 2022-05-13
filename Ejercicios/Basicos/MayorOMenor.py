x=int(6)

y=input("Introduzca un numero: ")

if (y.isdigit()):
    y=int(y)
    if (x>=y):
        print(f"{x} es mayor")
    else:
        print(f"{y} es mayor")
else:
    print("Introduzca un numero valido")