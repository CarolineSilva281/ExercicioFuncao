# Função para juntar nome e sobrenome
def nome_completo(nome, sobrenome):
    return f"{nome} {sobrenome}"  # Retorna a junção do nome e sobrenome

# Solicitando o nome e sobrenome ao usuário
nome_usuario = input("Digite seu nome: ")
sobrenome_usuario = input("Digite seu sobrenome: ")

# Exibindo o nome completo
print(f"Seu nome completo é: {nome_completo(nome_usuario, sobrenome_usuario)}")
