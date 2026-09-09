corridas = []


def cadastrar_corrida():
    print("\n---- Cadastro de Corridas ----")

    nome = input("Nome do Corredor: ")

    distancia = int(input("Distância percorrida em km: "))

    if distancia < 0:
        print("ERRO! Distância não pode ser negativa.")
        return

    tempo = int(input("Tempo decorrido em minutos: "))

    if tempo < 0:
        print("ERRO! Tempo não pode ser negativo.")
        return

    corrida = {
        "nome": nome,
        "distancia": distancia,
        "tempo": tempo
    }

    corridas.append(corrida)

    print("Corrida cadastrada com sucesso!")


def calcular_media():
    print("\n--- Média dos Corredores ---")

    total_distancias = 0
    quantidade_corridas = 0

    for corrida in corridas:
        total_distancias += corrida["distancia"]
        quantidade_corridas += 1

    if quantidade_corridas == 0:
        print("Nenhuma corrida cadastrada.")
        return

    media_distancias = total_distancias / quantidade_corridas

    print(f"Média das distâncias: {media_distancias}")


def corrida_mais_longa():
    print("\n--- Corrida mais Longa ---")

    if not corridas:
        print("Nenhuma corrida cadastrada.")
        return

    corrida_mais_longa = corridas[0]

    for corrida in corridas:
        if corrida["distancia"] > corrida_mais_longa["distancia"]:
            corrida_mais_longa = corrida

    print(f"Corredor: {corrida_mais_longa['nome']}")
    print(f"Distância: {corrida_mais_longa['distancia']} km")
    print(f"Tempo: {corrida_mais_longa['tempo']} minutos")


def menu():
    while True:
        print("\n==== Sistema de Registro de Corridas ====")
        print("1 - Cadastrar Corrida")
        print("2 - Calcular média")
        print("3 - Corrida mais longa")
        print("0 - SAIR")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_corrida()

        elif opcao == "2":
            calcular_media()

        elif opcao == "3":
            corrida_mais_longa()

        elif opcao == "0":
            print("SISTEMA ENCERRADO")
            break

        else:
            print("Opção Inválida!")


menu()