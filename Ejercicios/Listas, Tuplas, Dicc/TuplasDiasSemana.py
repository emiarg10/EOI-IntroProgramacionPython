dias=('Lun','Mar','Mie','Jue','Vie','Sab','Dom')
for dia in dias:
    print(dia)

for dia_numero in enumerate(dias,1):
    print(dia_numero)

#letras ='a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'
letras= 'abcdefghijklmnñopqrstuvwxyz'

letrasdelalfabeto=tuple(x for x in letras) #asi se crea una tupla de manera dinamica, para no ir una a una como arriba
for letra in enumerate(letrasdelalfabeto,40):
    print("letra: ", letra)

#Desempaquetar los valores de la tupla

postres =('tiramisu','flan','pudin')
#unpaking
postrea,postreb,postrec=postres

nuevospostres=(postrea,postreb,postrec)
print ("Postres en la nueva tupla, R=YES: ", nuevospostres)
print ("Postres en la tupla: ", postres)
print ("Valores unpacking: ", postrea,postreb,postrec)