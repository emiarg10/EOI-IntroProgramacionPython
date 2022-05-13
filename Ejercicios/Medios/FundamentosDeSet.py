ciudades={'Madrid','Albacete','Vigo','Palencia','Sevilla','Vigo','Vigo','Sevilla'}
print (ciudades)
ciudades.add('Valencia')
ciudades.add('Gijon')
print(ciudades)
for ciudad in ciudades:
    print(ciudad)
ciudades.discard('Palencia')
print('Conjunto (SET) de ciudades despues de borrar Palencia:')
for ciudad in ciudades:
    print(ciudad)