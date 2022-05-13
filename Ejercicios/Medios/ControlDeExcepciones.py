numero1 = 100
numero2 = 50
a= "2"


try:
    print("otra instruccion1")
    print("otra instruccion2")
    print(numero1/numero2)
    print("otra instruccion3")
    c=int(a)
    print("otra instruccion4")

except ZeroDivisionError:
        print("Error al dividir por cero.")

except ValueError:
        print("Error al convertir un texto a numero")
        
except:
        print("Error")
        
else:
        print("La instrucciones se completaron correctamente")

finally:
        print("Fin del programa")
