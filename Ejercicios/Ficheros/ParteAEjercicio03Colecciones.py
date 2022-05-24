from genericpath import exists
from logging import exception
from random import randint
from ParteAEjercicio02Colecciones import lee_o_crea_fichero as lee_escribe
import random
print(f'Ejecucion03:{__name__}')
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


fileChicos = './Ficheros/Data_Chicos_Ejercicios03.txt'
fileChicas = './Ficheros/Data_Chicas_Ejercicio03.txt'

lee_escribe(fileChicos,DiccHombres)
lee_escribe(fileChicas,DiccChicas)
