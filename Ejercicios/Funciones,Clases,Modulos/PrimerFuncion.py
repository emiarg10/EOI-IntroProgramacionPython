def saludar(nombre):
    print(f"Hola {nombre}")

def sumar(a,b):
    return(a+b)

def addColores(colores,color):
    try:    
        colores.append(color)
        return True
    except AttributeError:
        return False

saludar('Emi')
saludar('Javi')
saludar('Juan')

print (sumar(5,5))
print (sumar(2,6))
print (sumar(9,9))
print (sumar(4,2))

colores = []
addColores(colores, 'azul')
addColores(colores, 'rojo')
addColores(colores, 'verde')
addColores(colores, 'negro')
addColores(colores, 'amarillo')
print(colores)
saludar(colores)

if (addColores('billy','naranja')): #if (True==False)
    print("Se ha insertado")
else:
    print("No se ha insertado")

