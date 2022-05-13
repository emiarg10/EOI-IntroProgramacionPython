#Leer tres números; si el primero es negativo, debe imprimir la multiplicación de los tres y si no lo es, imprimirá la suma.

num1 = input("Ingrese numero1: ")
num2 = input("Ingrese numero2: ")
num3 = input("Ingrese numero3: ")
resul = 0

try:
    num1=float(num1)
    num2=float(num2)
    num3=float(num3)

    if num1<0:
        resul = num1*num2*num3
        print (f"El resultado de la multiplicacion es: {resul}")

    else:
        resul = num1+num2+num3
        print (f"El resultado de la suma es: {resul}")

except:
    print("Introduzca un numero valido")
