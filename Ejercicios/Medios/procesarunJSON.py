import json
jsonventas = '{"departamento":8,"nombredepto":"Ventas","director":"Juan Rodriguez","empleados":[{"nombre":"Pedro","apellido":"Fernandez"},{"nombre":"Jacinto","apellido":"Benavente"}]}'
print(jsonventas)
print(type(jsonventas))

datosDepartamento = json.dumps(jsonventas) # Serializacion de un objeto a JSON (JSON es un string)
print(type(datosDepartamento))

jsonventas = json.loads(jsonventas) # Deserializacion de un JSON a Objeto
print(type(jsonventas))


print('Json 1', datosDepartamento)



# Conlusion:
# La variable que debo utilizar para procesar el JSON como una coleccion compleja(compuesta) es el deserealizado (loads)

for val in jsonventas:
    if val!='empleados':
        print(val,':', jsonventas[val])

    else:
        print('Integrantes de ldepartamento: ')
        for integrantes in jsonventas['empleados']:
            print('\t\t', integrantes['nombre'],'', integrantes['apellido'])

#for val in datosDepartamento: #ESTO PROCESARA UN STRING
#    print("DatosDpto: " , val)