numeros = [10, 15, 20, 25, 30, 35, 40, 45, 50]

numeros[::2]     # [10, 20, 30, 40, 50]  → do início ao fim, de 2 em 2
numeros[1::2]    # [15, 25, 35, 45]      → começa no índice 1, de 2 em 2
numeros[:5]      # [10, 15, 20, 25, 30]  → do início até o índice 5 (exclusivo)
numeros[::]      # [10, 15, 20, 25, 30, 35, 40, 45, 50]  → tudo, sem alterar nada
numeros[::-1]    # [50, 45, 40, 35, 30, 25, 20, 15, 10]  → passo -1 inverte a lista!