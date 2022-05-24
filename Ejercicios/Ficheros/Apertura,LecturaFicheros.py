'''def fichero_existe(file):
    try:
        open(file) #equivale a open(file,'rt')

    except FileNotFoundError:
        return False

    return True
'''

from genericpath import exists


try:
    file = 'file_500.csv'
    #fichero_existe = True

    if (exists(file)):
        fichero = open(file,'rt',encoding='UTF-8')
        contenido = fichero.read()
        if (len(contenido)>0):
            print (contenido)
        else:
            print ('El fichero no tiene contenido')
    else:
        fichero = open(file,'wt',encoding='UTF-8')
        contenido = f'{file}, fichero501, arbol, limon, mandarina'
        fichero.write(contenido)
        print ('Escrito el contenido')

except FileNotFoundError as e:
    print(f'E: {e}')

except Exception as e:
    print(f'E: {e}')

finally:
    fichero.close()
    print('closing')