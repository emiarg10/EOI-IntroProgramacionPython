#Se ha definido una clase que representa un inventario de aviones. También se crea una instancia de esta clase Jet y se asigna a la variable first_item. Imprimir el nombre del primer_elemento.
#Ahora imprima el origen del primer_elemento.
from telnetlib import XASCII
from unicodedata import category


class Jets:
    model = None
    country = 0
    def __init__(self, name, country,quantify=0):
        self.name = name
        self.origin = country
        self.quantify = quantify

    def __str__(self):
        return '{} -> {}'.format(self.name,self.origin)    

first_item = Jets("F16", "USA")


a = first_item.name
b = first_item.origin

print(a)
print(b)

#Cree nuevas instancias hasta el sexto elemento siguiendo este orden: F14, SU33, AJS37, Mirage2000, Mig29, A10.
#Puede tener en cuenta que los orígenes son:
#F14: USA SU33: Russia AJS37: Sweden Mirage2000: France Mig29: USSR A10: USA

first_item= Jets('F14','USA')
second_item= Jets('SUB33','RUSSIA')
third_item= Jets('AJS37','SWEDEN')
fourth_item= Jets('MIRAGE2000','FRANCE')
fifth_item=Jets('MIG29','USSR')
sixth_item=Jets('A10','USA')
#first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
first_army=[str(first_item),str(second_item),str(third_item),str(fourth_item),str(fifth_item),str(sixth_item)]

print(first_army)


#Agregue otro atributo llamado "cantidad" al método de inicialización (generalmente denominado constructor o init).
#Luego defina "asignar" este atributo al atributo self.quantity dentro del constructor.
#Luego cree 2 instancias para: F14 y Mirage2000 con cantidades 87 y 35.

first_item= Jets('F14','USA', 87)
second_item= Jets('SUB33','RUSSIA', 35)
total = first_item.quantify + second_item.quantify
print('Respuesta Ej:4 -> ', total)

#Construir una clase simple desde cero. Ya se ha creado una instancia para usted y los atributos de la instancia se incluyen dentro del print. Tome esas pistas y con estos datos cree la clase.

class Nobel:
    def __init__(self,category,year,winner):
        self.category = category
        self.year = year
        self.winner = winner 
    
    def __str__(self):
        return'{} {} {}'.format(self.category,self.year,self.winner)
        

nq2019=Nobel("\nChemistry", 2019, "John B. Goodenough")

print(nq2019.category, nq2019.year, nq2019.winner)

#Construir una clase simple desde cero. Es la misma que el ejercicio anterior, ahora usará la función __ str __ para devolver una representación de cadena para la clase cuando sea necesario.

print(nq2019)

#Cree una clase llamada myfunc y dentro de ella coloque una función muy simple llamada "quinta" que toma x y devuelve la quinta potencia de x. No se necesitan init o atributos de clase.
#Finalmente llame a su función con el número 5 y asígnela a la variable ans.

class myfunc:
    def ElevarAlaPotencia(x,y):
        return x**y
    
    def __str__(self):
        return 'Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia.'
    
ans = myfunc.ElevarAlaPotencia(5,5)
print(ans)

#Ahora hagamos algunos cambios en la clase que creamos en el ejercicio anterior de Python.
#Primero haga su función para que tome los parámetros: x e y. x será el número que se eleva, e será la potencia. ¡Entonces, los usuarios pueden elevar los números a cualquier potencia!
#También cambiemos el nombre de la función a "ElevarAlaPotencia".
#También agreguemos una representación de cadena rápidamente, de modo que cuando un usuario imprima la clase obtenga una descripción significativa.
#Puede ser algo como: Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia.
ans2 = myfunc()
print(ans2)
x = input ("Introducir numero que desea elevar: ")
y = input('Introducir la potencia: ')



try:
    x=float(x)
    y=float(y)
    ans1 = myfunc.ElevarAlaPotencia(x,y)
    print(ans1)
    

except:
    print('Introduzca unos numeros validos.')