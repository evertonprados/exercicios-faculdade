estoque = []


def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")

    codigo = input("Código: ")

    for produto in estoque:
        if produto["codigo"] == codigo:
            print("Erro: código já cadastrado!")
            return

    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    if preco < 0:
        print("Erro: o preço não pode ser negativo!")
        return

    if quantidade < 0:
        print("Erro: a quantidade não pode ser negativa!")
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    estoque.append(produto)

    print("Produto cadastrado com sucesso!")


def calcular_total():
    print("\n--- Total de Produtos em Estoque ---")

    total = 0

    for produto in estoque:
        total += produto["quantidade"]

    print(f"Quantidade total: {total}")


def menu():
    while True:
        print("\n===== CONTROLE DE ESTOQUE =====")
        print("1 - Cadastrar Produto")
        print("2 - Calcular Total de Produtos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            calcular_total()

        elif opcao == "0":
            print("Sistema encerrado!")
            break

        else:
            print("Opção inválida!")


menu()