colores = ["Red","Yellow","Green"]
colores_alternativos = ["Magenta","Blue","Pink"]
colores.extend(colores_alternativos)
colores.sort() # orden ascendente
print ("Lista de colores actualizada despues del sort: ", colores)

colores.sort(reverse=True)
print("La lista actualizada despues del sort descendente es: ", colores)
