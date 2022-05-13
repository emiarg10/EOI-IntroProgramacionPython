diccColores = {"red":"rojo", "blue":"azul", "green":"verde"}
print ("Diccionario inicial:", diccColores)
diccColores["black"] = "negro" # añadir elemento al diccionar dado su clave:valor
print("Diccionario despues de añadir el color negro", diccColores)
diccColores.pop("green") # quitar un elemento del diccionario dado su clave
print("Diccionario despuies de quitar el color verde", diccColores) 

print("Red en castellano: ", diccColores["red"])
print("Blue en castellano: ", diccColores["blue"])

for key in diccColores:
    print(key, '->',diccColores[key]) 