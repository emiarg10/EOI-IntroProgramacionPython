from random import randint
listachicas = []
listachicos = []

for i in range(1,101):
    genero = randint(0,1)
    if genero == 1:
        listachicas.append(f"chica{i}")
    else:
        listachicos.append(f"chico{i}")
        
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
