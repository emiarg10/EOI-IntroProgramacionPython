#Hacer un programa que procese un total de 100 personas y establecer cuantas son mujeres mayores de edad y cuantos hombres menores de edad. Deberá sacar el hombre y la mujer con menor edad, el hombre y
#la mujer con mayor edad, promedio de edades de las mujeres y promedio de edades de los hombres.

from random import randint
import random

DiccHombres={}
DiccChicas={}
chicosmenores = 0
chicasmayores = 0

for i in range(1,101):
    genero = randint(0,1)
    edades = randint(1,100)
    if (genero==0):                                         # Si es hombre se añade un hombre y su edad al diccionario
        DiccHombres[f'Hombre {i}'] = edades
        if edades<18:                                       # Si es menor de edad de suma un hombre menor de edad a la variable "chicosmenores"
            chicosmenores+=1
    else:                                                   # Si es mujer se añade una mujer y su edad al diccionario
        DiccChicas[f'Mujer {i}'] = edades 
        if edades>=18:                                      # Si es mayor de edad de suma una mujer mayor a la variable "chicasmayores"
            chicasmayores+=1                                


tuplaHombres = DiccHombres.values() # Creamos una tupla con las edades de los hombres
tuplaMujeres = DiccChicas.values() # Creamos una tupla con las edades de las mujeres

print('Hay una cantidad de:', chicosmenores, 'chicos menores de edad\n')
print('Hay una cantidad de:', chicasmayores, 'chicas mayores de edad\n')

print ('El hombre mas viejo tiene:', max(tuplaHombres), 'años\n')
print ('El hombre mas joven tiene:', min(tuplaHombres), 'años\n')

print ('La mujer mas vieja tiene:', max(tuplaMujeres), 'años\n')
print ('La mujer mas joven tiene:', min(tuplaMujeres), 'años\n')


print ('El promedio de edad de los hombres es de:', sum(tuplaHombres)/len(tuplaHombres))

print ('El promedio de edad de los hombres es de:', sum(tuplaMujeres)/len(tuplaMujeres))

