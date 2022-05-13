from datetime import datetime

# Fechas y Horas

datenow1=datetime.now().date()
print("Fecha1: ",datenow1)
print("Año Fecha1: ",datenow1.year)
print("Mes Fecha1: ",datenow1.month)
print("Dia Fecha1: ",datenow1.day)
# print("Hora Fecha1: ",datenow1.hour) No esta disponible por que la variable solo contiene la fecha

datenow2=datetime.now()
print("Fecha2: ",datenow2)
print("Año Fecha2: ",datenow2.year)
print("Mes Fecha2: ",datenow2.month)
print("Día Fecha2: ",datenow2.day)
print("Hora Fecha2: ",datenow2.hour)
print("Minuto Fecha2: ",datenow2.minute)
print("Segundos Fecha2: ",datenow2.second)
print("Microsegundos Fecha2: ",datenow2.microsecond)
print(f"Hora2:{datenow2.hour}",datenow2.hour)

datenow3=datetime.now()
print("Fecha3: ",datenow3)
print("Año Fecha3: ",datenow3.year)
print("Mes Fecha3: ",datenow3.month)
print("Día Fecha3: ",datenow3.day)
print("Hora Fecha3: ",datenow3.hour)
print("Minuto Fecha3: ",datenow3.minute)
print("Segundos Fecha3: ",datenow3.second)
print("Microsegundos Fecha3: ",datenow3.microsecond)
print(f"Hora3:{datenow3.hour}:{datenow3.minute}")