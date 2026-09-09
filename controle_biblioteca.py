biblioteca = []


def cadastrar_livro():
    print("\n---- CADASTRO DE LIVROS ---")

    codigo = int(input("Digite o código do Livro: "))

    if codigo < 0:
        print("ERRO! Código não pode ser negativo.")
        return

    for livro in biblioteca:
            if livro["codigo"] == codigo:
                print("Erro: Código já cadastrado!")
                return

    titulo = input("Título do Livro: ")
    autor = input("Autor: ")
    quantidade = int(input("Quantidade: "))

    if quantidade < 0:
            print("ERRO! Quantidade não pode ser negativa")
            return
    
    livro = {
            "codigo" : codigo,
            "titulo" : titulo,
            "autor" : autor,
            "quantidade" : quantidade }

    biblioteca.append(livro)
    print("Livro cadastrado com sucesso!")

def registrar_emprestimo():
    print("\n---- Registrar Empréstimo ----")

    emprestimo = int(input("Digite o Código do Livro: "))

    encontrado = False   # começa como "ainda não achei"

    for livro in biblioteca:
        if livro["codigo"] == emprestimo:
            encontrado = True   
            if livro["quantidade"] > 0:
                livro["quantidade"] -= 1
                print(f"Empréstimo registrado: {livro['titulo']}")
            else:
                print("Erro: não há exemplares disponíveis para este livro!")

    if not encontrado:
        print("Erro: código não encontrado!")

def calcular_total():
        print("\n--- Total de Livros na Biblioteca ---")

        total = 0
        for livro in biblioteca:
            total += livro["quantidade"]

        print(f"Quantidade total : {total}")

def menu():
     while True:
          print("\n---- CONTROLE DA BIBLIOTECA ----")
          print("1 - Cadastrar Livro")
          print("2 - Registrar Empréstimo")
          print("3 - Calcular Total de Livros")
          print("0 - SAIR")

          opcao = input("Escolha uma opção: ")

          if opcao == "1":
               cadastrar_livro()
          elif opcao == "2":
               registrar_emprestimo()
          elif opcao == "3":
               calcular_total()
          elif opcao == "0":
               print("SISTEMA ENCERRADO")
               break
          else:
               print("Opção Inválida!")

menu()



    














