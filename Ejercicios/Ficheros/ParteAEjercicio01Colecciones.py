from genericpath import exists
from logging import exception
from random import randint
listachicas = []
listachicos = []

for i in range(1,101):
    genero = randint(0,1)
    if genero == 1:
        listachicas.append('0')
    else:
        listachicos.append('1')
        
numerochicas = len(listachicas)
numerochicos = len(listachicos)

print (f"Hay una cantidad de {numerochicas} chicas. Equivalente al {(numerochicas*100)/100}%")
print (f"Hay una cantidad de {numerochicos} chicos. Equivalente al {(numerochicos*100)/100}%")

if (numerochicas>numerochicos):
    print("El numero de chicas es mayor al numero de chicos")
elif (numerochicas<numerochicos):
    print("El numero de chicos es mayor al numero de chicas")
else:
    print("Hay la misma cantidad de chicas y chicos.")


listaentera = listachicas + listachicos
print(listaentera)
try:
    file = './Ficheros/Datos_Ejercicios01.txt'

    if (exists(file)):
        print ('Fichero previamente generado no se sobrescribe')
        fichero = open(file,'rt',encoding='UTF-8')
        contenido = fichero.read()
        print (f'El contenido del fichero es: \n{contenido}')
    else:
        fichero = open(file,'wt',encoding='UTF-8')
        fichero.write(str(listaentera))

except exception as e:
    print(f'E: {e}')

finally:
    
    fichero.close()