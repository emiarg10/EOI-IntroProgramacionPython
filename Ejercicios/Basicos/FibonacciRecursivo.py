def fibonacci(N):
    if (N==1):
        return 0
    elif(N==2):
        return 1
    else:
        return (fibonacci(N-1)+fibonacci(N-2))

n=input('Que numero de la serie Fibonacci quiere?: ')

try:
    n=int(n)
    seriefibo=[]
    for i in range(1,n+1):
        r = fibonacci(i)
        seriefibo.append(r)
    print(f'El nunmero en esa posicion es: {r}')
    print('La serie es:', *seriefibo)

except TypeError:
    print('Numero no valido')
except:
    print('Ingrese un numero valido')