print("Instruccion antes del While")
valor = 0

while(valor<5):
    valor+=1

    if (valor>3):
        #continue
        break
    print(f"El valor es {valor}")

print("Instruccion despues del While")