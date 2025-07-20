# Função para contar as letras em uma frase
def contar_letras(frase):
    count = 0  # Variável para contar as letras
    for char in frase:
        if char != ' ':  # Verifica se o caractere não é um espaço
            count += 1  # Incrementa o contador
    return count

# Solicitando uma frase ao usuário
frase_usuario = input("Digite uma frase: ")
print(f"A quantidade de letras na frase é: {contar_letras(frase_usuario)}")
