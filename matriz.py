# Matriz 3x3 usando listas aninhadas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elemento específico: matriz[linha][coluna]
print(matriz[1][2])   # 6 (linha 1, coluna 2)

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()   # pula linha ao terminar cada linha da matriz

# Saída:
# 1 2 3
# 4 5 6
# 7 8 9
