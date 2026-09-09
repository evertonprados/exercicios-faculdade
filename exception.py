try:
    # código que pode dar erro
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        raise ValueError("Idade deve ser maior ou igual a 18.")
except ValueError as e:
    # trata o erro, caso ele aconteça
    print(f"Erro: {e}")
else:
    # roda só se NÃO deu erro nenhum
    print("Idade válida!")
finally:
    # roda sempre, com ou sem erro
    print("Fim da verificação.")