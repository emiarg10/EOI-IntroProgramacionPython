from typing import Type


def Factorial(N):
    if N<=0:
        #Esto queda pendiente ...
        #generar una excepcion
        raise
        #pass

    if (N<=1):
        print('return 1')
        return 1
    else:
        print('return {} Factorial({}-1)'.format(N,N))
        return N * Factorial(N-1)


n=input('De que numero desea calcular el factorial: ')
try:
    n=int(n)
    r=Factorial(n)
    print ('El factorial de:',n, 'es',r)
except TypeError:
    print ('Ingrese un numero valido')
except:
    print('No se permiten valores menores a 0')
