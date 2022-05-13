def procesoinicial():
    print('Buscar una hoja de papel')

def procesoDos():
    print('Doblar la hoja')

def SaludarATodos(*nombres):
    for i in nombres:
        print(f'Hola {i}')

def SaludarATodosDicc(**nombres):
    for i in nombres:
        print(f"Hola: {i} {nombres[i]}")

def ciudades(pais, ciudad='Malaga'):
    print(pais,'', ciudad)

procesoinicial()
procesoDos()
colores=['azul','rojo','amarillo']
SaludarATodos('Emi')
SaludarATodos('Jose','Diego','Messi','Cr9')
SaludarATodos('Marado','Alvaro','David')
SaludarATodos('Emi',True,345)
SaludarATodos(colores,'John')

SaludarATodosDicc(nombre='Billy', apellidos='Vanegar')
SaludarATodosDicc(nombre='Emi', apellido='Cr9')

ciudades('Argentina')
ciudades('mexico', 'Ciudad de mexico')