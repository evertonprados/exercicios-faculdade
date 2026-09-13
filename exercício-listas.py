numeros = [10, 20, 30, 40, 50]
for cronometro in range(len(numeros)):
    if numeros[cronometro] == 30:
        print("Encontrado no índice:", cronometro)
        break   # interrompe assim que encontra — evita checagens desnecessárias
