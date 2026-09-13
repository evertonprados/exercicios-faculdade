mensagem_global = "Olá, bem-vindo ao programa!"  # variável global

def saudacao(nome):
    """Função que usa uma variável global e uma variável local."""
    mensagem_local = f"Olá, {nome}! Tenha um ótimo dia!"  # variável local
    print(mensagem_global)   # OK — acessando variável global
    print(mensagem_local)    # OK — acessando variável local

saudacao("Lucas")

# print(mensagem_local)  # ERRO! mensagem_local não existe fora da função
