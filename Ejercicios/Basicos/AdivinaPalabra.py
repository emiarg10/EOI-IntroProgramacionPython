palabra1 = "suerte"
print("Adivine la palabra (N para abandonar): ")

while True:

    palabra2 = input().lower() # Ahorrando asignar palabra2 = palabra2.lower()

    if palabra2 == palabra1:

        break # Ahorrando tener una variable boolean comprobando el estado
    else:
        print("Vuelve a intentarlo: ")

print("Felicidades, has adivinado la palabra")