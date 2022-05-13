while (True):
    nombre = input("Escribir un nombre: ")
    cantidad = input ("Escribir cantidad: ")

    try:
        
        if (not nombre.isdigit()):
            if (cantidad.isnumeric):
                cantidad=int(cantidad)

            while (cantidad>0):
                print(nombre)
                cantidad-=1
        else:
            print("Por favor introduzca un nombre valido")

    except ValueError:
            print("Error, Escriba un numero entero")

    salir = input("Pulse N para salir\n")
    if (salir=="N" or salir=="n"):
        print ("Bye!, Gracias por usar este programa\n")
        break

