from random import randint
listamayoresedad = []
listatodasedades = []
diccionarioedades = {}

for i in range(1,101):
    edades = randint(1,100) # Generamos edades aleatorias entre 1 y 100 años.
    listatodasedades.append(edades) # Añadimos a la lista todas las edades.
    

    if (edades>=18):
        listamayoresedad.append(edades) # Añadimos a la lista las edades mayores de edad

tuplaedades = tuple(listatodasedades) # Convertimos la lista con todas las edades a una tupla para luego poder saber la edades minima y maximas. Ya que en una tupla no se pueden añadir

for j in range(1,101): 
    contadoredades = tuplaedades.count(j) # contamos la cantidad de edades que se repiten.
    diccionarioedades.setdefault(j,contadoredades) # añadimos cada edad junto a las veces que se repite a un diccionario.

#print("Todas las edades: ", tuplaedades) # Hacemos un print de todas las edades.

print(f"Hay un total de {len(listamayoresedad)} personas mayores de edad")
print(f"La persona mas joven tiene: {min(tuplaedades)} años")
print(f"La persona mas vieja tiene: {max(tuplaedades)} años")
print(f"La media de edad es de: {(sum(tuplaedades)/100)} \n")


for valor in diccionarioedades: # Analizamos la clave:valor del diccionario y mostramos el porcentaje de su valor. En este caso el porcentaje que se repite esa edad.
    print('Los porcentajes de edad son: \n',valor, '->', (diccionarioedades[valor]*100)/100, '%') 

