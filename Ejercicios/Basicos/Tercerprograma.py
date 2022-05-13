ciudad = "madrid"
print (ciudad.isdigit())
minombre = "Emiliano"
print (len(minombre))

print (minombre[0])
print (minombre[1])
print (minombre[2])
print (minombre[2:])
print (minombre[:3])
print (minombre[2:4])
print (minombre[-4])

mensaje = "Emi"
print ("Hola {}".format(mensaje))
print ("Hola " + mensaje)
print ("Hola {m} de {c}".format (m=mensaje, c=ciudad))

numero = 10/3
print ("El numero sin formato es:{}".format(numero))

print ("El numero con formato es:{n:1.2f}".format(n=numero))

print (f"Hola {mensaje} de {ciudad}")