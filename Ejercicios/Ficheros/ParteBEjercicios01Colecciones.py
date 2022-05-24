from genericpath import exists
from typing import final

def Proceso(contenido):
    try:
        file_resultado='./Ficheros/Resultado_Ejercicios01_1.txt'
        fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
        lista = contenido
        fichero_resultado.write(f'El procentaje de mujeres es del: {lista.count("1")}%\n')
        fichero_resultado.write(f'El porcentaje de hombres es del: {lista.count("0")}%\n')

        if (lista.count('0')) > lista.count('1'):
            fichero_resultado.write('Hay mas mujeres que chicas\n')
        elif(lista.count('0') < lista.count('1')):
            fichero_resultado.write('Hay mas mujeres que hombres')
        else:
            fichero_resultado.write('Hay igualdad de hombres y mujeres\n')

    except Exception as e:
        print(f'E: {e}')

try:
    file = './Ficheros/Datos_Ejercicios01.txt'

    if (exists(file)):
        fichero = open(file,'rt',encoding='UTF-8')
        contenido = fichero.read()
        Proceso(contenido)
    else:
        print('No podemos procesar la informacion')

except Exception as e:
    print(f'E: {e}')

finally:
    fichero.close()

