import math
pi = math.pi
r = input("Introducir el radio del cilindro: ")
h = input("Introducir la altura del cilindro: ")

try:
    h=float(h)
    r=float(r)
    
    area = 2*pi*(r*r)
    volumen = pi*(r*r)*h
    print (f"El area del cilindro es: {area:1.2f} m^2")
    print (f"El volumen del cilindro es: {volumen:1.2f} m^3")

except:
    print("Introduzca unos datos validos")