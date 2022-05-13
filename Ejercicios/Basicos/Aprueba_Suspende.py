# Determinar si un alumno aprueba o suspende un curso, si su media de las 3 notas es mayor o igual a 4.0 y calcular su media
cal1=input("Ingrese calificacion 1: ")
cal2=input("Ingrese calificacion 2: ")
cal3=input("Ingrese calificacion 3: ")


try:
    cal1=float(cal1)
    cal2=float(cal2)
    cal3=float(cal3)

    if (0<=cal1<=10) and (0<=cal2<=10) and (0<=cal3<=10):
        prom=(cal1+cal2+cal3)/3

        if (prom>=4):
            print(f"El alumno aprueba el curso. Su media es de {prom}")

        else:
            print(f"El alumno suspende el curso. Su media es de {prom}")

    else:
        print("El rango de las calificaciones es erroneo. Por favor, introduzca notas entre 0 y 10")

except ValueError:
    print("Error, Ingrese calificaciones numericas")
