from genericpath import exists

def SegundaParte():
    file = './Ficheros/Data_ejercicios04.txt'
    fichero = None
    
    try:
        fichero = open(file,'rt',encoding='UTF-8')
        contenido = fichero.read()
        fichero.close()
        ciudad_temperaturas = eval(contenido)
        ciudad_promedios = {}

        for ciudad,grados in ciudad_temperaturas.items():
            ciudad_promedios[ciudad] = sum(grados)/len(grados)
        mas_alta=max(ciudad_promedios, key=ciudad_promedios.get)
        mas_baja=min(ciudad_promedios, key=ciudad_promedios.get)

        promedios_ordenados = sorted (ciudad_promedios, key=ciudad_promedios.get, reverse=True)



        file_resultado = './Ficheros/Resultado_Ejercicios04.txt'
        fichero_resultado = open(file_resultado,'wt',encoding='UTF-8')
        sl = '\n'
        tb = '\t'
        linea = '{}{}'.format('='*100,sl)
        fichero_resultado.write(f'Resultado del ejercicio 05 de colecciones con ficheros{sl}')
        fichero_resultado.write(linea)
        fichero_resultado.write('La ciudad con el promedio anual mas alto es: {} -> {:1.2f}ºC{}'.format(mas_alta,ciudad_promedios[mas_alta],sl))
        fichero_resultado.write('La ciudad con el promedio anual mas baja es: {} -> {:1.2f}ºC{}'.format(mas_baja,ciudad_promedios[mas_baja],sl))
        columna = 1
        fichero_resultado.write(sl)
        fichero_resultado.write(f'Resumen de las ciudades con las temperaturas mas altas del año (ordenadas ascendentemente){sl}')
        fichero_resultado.write(linea)
        for ciudad in promedios_ordenados:
            fichero_resultado.write('{}{:12}{:1.2f} ºC{}'.format(tb,ciudad,float(ciudad_promedios[ciudad]),sl if columna%3 == 0 else tb))
            columna+=1
        fichero_resultado.write(f'{sl}{linea}')

        print('Datos guardados con exito!.')

    except Exception as e:
        print(f'E: {e}')
    finally:
        if fichero!=None:
            fichero.close()

if __name__ == '__main__':
    SegundaParte()