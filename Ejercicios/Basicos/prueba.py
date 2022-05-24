frase = 'holawacho gil'

print(frase.strip('ch'))

def saludar(nombre='emi'):
    print(nombre)

saludar()
saludar('fali')

saludarse = lambda nombre='emi':print(nombre)

saludarse()
saludarse('papitas')