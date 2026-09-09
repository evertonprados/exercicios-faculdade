# Ordenar uma lista de tuplas pelo segundo elemento
alunos = [("Ana", 8), ("Bruno", 5), ("Carla", 9)]
alunos_ordenados = sorted(alunos, key=lambda x: x[1])
print(alunos_ordenados)
# [('Bruno', 5), ('Ana', 8), ('Carla', 9)]

# Filtrar números pares com filter()
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

# Aplicar uma transformação com map()
numeros = [1, 2, 3]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6]