# Função para mostrar as letras de uma palavra
def mostrar_letras():
    # Pede para o usuário digitar uma palavra
    palavra = input("Digite uma palavra: ")
    
    # Laço for para percorrer cada letra da palavra
    for letra in palavra:
        print(letra)  # Exibe a letra atual

# Chamando a função
mostrar_letras()
