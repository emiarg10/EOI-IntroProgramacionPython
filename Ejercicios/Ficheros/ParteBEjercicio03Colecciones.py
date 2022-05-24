
from genericpath import exists

def ProcesarArchivos(contenido, nombreresultado):
    try:
        if (nombreresultado == './Ficheros/Resultado_Ejercicios03.txt'):
            file_resultado = nombreresultado
            fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
            lista = eval(contenido)
            valores = [lista[valores] for valores in lista]
            fichero_resultado.write(f'Hay una cantidad de: {len([lista[valores] for valores in lista if lista[valores]>=18])} chicas mayores de edad\n')
            fichero_resultado.write(f'Las mujer mas vieja tiene: {max(lista)} años\n')
            fichero_resultado.write(f'Las mujer mas joven tiene: {min(lista)} años\n')
            fichero_resultado.write(f'El promedio de edad de las mujeres es de: {round(sum(valores)/len(lista), 2)}%')

        else:
            file_resultado = nombreresultado
            fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
            lista = eval(contenido)
            valores = [lista[valores] for valores in lista]
            fichero_resultado.write(f'Hay una cantidad de: {len([lista[valores] for valores in lista if lista[valores]<18])} chicos menores de edad\n')
            fichero_resultado.write(f'El hombre mas viejo tiene: {max(lista)} años\n')
            fichero_resultado.write(f'El hombre mas joven tiene: {min(lista)} años\n')
            fichero_resultado.write(f'El promedio de edad de los hombres es de: {round(sum(valores)/len(lista), 2)}%')
            
    except Exception as e:
        print(f'E: {e}')


def leerArchivos (file_nombre, nombreresultado):
    try:
        
        if exists(file_nombre):
            fichero = open(file_nombre,'rt', encoding='UTF-8')
            contenido = fichero.read()
            ProcesarArchivos(contenido, nombreresultado)
            print ('Archivo leido')
        else:
            print('Error. No podemos procesar la informacion')
    except Exception as e:
        print(f'E: {e}')
    finally:
        fichero.close()       

file = './Ficheros/Data_Chicas_Ejercicios03.txt'
file1 = './Ficheros/Data_Chicos_Ejercicios03.txt'



leerArchivos(file, './Ficheros/Resultado_Ejercicios03.txt')
leerArchivos(file1, './Ficheros/Resultado_Ejercicios03B.txt')