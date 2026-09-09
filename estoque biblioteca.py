biblioteca = []

def cadastrar_livro():
    print("\n--- Cadastro de Livros: ")

    codigo = input("Código: ")

    for livro in biblioteca:
        if livro["codigo"] == codigo:
            print("Erro: Código já cadastrado!")
            return

    titulo = input("Título: ")
    autor = input("Autor: ")
    quantidade = int(input("Quantidade: "))


    if quantidade < 0:
        print("ERRO! Quantidade não pode ser negativa")
        return

    livro = {
        "codigo" : codigo,
        "titulo" : titulo,
        "autor" : autor,
        "quantidade" : quantidade
    }

    biblioteca.append(livro)

    print("Livro cadastrado com Sucesso!")

def calcular_total():
        print("\n--- Total de Livros na Biblioteca ---")

        total = 0
        for livro in biblioteca:
            total += livro["quantidade"]

        print(f"Quantidade total : {total}")

def menu():
        while True:
            print("\n==== CONTROLE DA BIBLIOTECA ====")
            print("1 - Cadastrar Livro")
            print("2 - Calcular Total de Livros")
            print("0 - SAIR")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cadastrar_livro()

            elif opcao == "2":
                calcular_total()

            elif opcao == "0":
                print("SISTEMA ENCERRADO")
                break

            else:
                print("Opção Inválida!")

menu()

