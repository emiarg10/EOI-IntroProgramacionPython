from genericpath import exists

def ProcesarArchivos(contenido, nombreresultado):
    try:
        if (nombreresultado == './Ficheros/Resultado_Ejercicios02.txt'):
            file_resultado = nombreresultado
            fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
            lista = eval(contenido)

            fichero_resultado.write(f"Hay un total de {len([x for x in lista if x>=18])} personas mayores de edad\n")
            fichero_resultado.write(f"La persona mas joven tiene: {min(lista)} años\n")
            fichero_resultado.write(f"La persona mas vieja tiene: {max(lista)} años\n")
            fichero_resultado.write(f"La media de edad es de: {(sum(lista)/100)} \n")

        else:
            file_resultado = nombreresultado
            fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
            lista = eval(contenido)
            fichero_resultado.write(f'Las edades repetidas son: {lista}')


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

if __name__ == '__main__':
    file = './Ficheros/Datos_Ejercicios02.txt'
    file1 = './Ficheros/Datos_Ejericicos02A.txt'
    leerArchivos(file, './Ficheros/Resultado_Ejercicios02.txt')
    leerArchivos(file1, './Ficheros/Resultado_Ejercicios02B.txt')