# Função para verificar se uma palavra é um palíndromo
def verificar_palindromo(palavra):
    # Compara a palavra com a palavra invertida
    if palavra == palavra[::-1]:  # Palavra[::-1] inverte a palavra
        return True
    else:
        return False

# Solicitando uma palavra ao usuário
palavra_usuario = input("Digite uma palavra: ")
if verificar_palindromo(palavra_usuario):
    print(f"A palavra {palavra_usuario} é um palíndromo!")
else:
    print(f"A palavra {palavra_usuario} não é um palíndromo.")
