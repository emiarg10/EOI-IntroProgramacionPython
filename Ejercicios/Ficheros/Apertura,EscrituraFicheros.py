file = 'file_300.txt'
fichero = open(file,'wt',encoding='UTF-8')
contenido = "'árbol' , 'limón' , 'naranja''"
fichero.write(contenido)
fichero.close()
#eval() 'pasar una cadena de caracteres lista, o diccionarioç
contenido = fichero.read()
diccCiudades = eval(contenido)
print('Fin de la cita..')