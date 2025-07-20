# Função para encontrar o maior número em uma lista
def maior_numero(lista):
    maior = lista[0]  # Assume que o primeiro número é o maior inicialmente
    for num in lista:
        if num > maior:
            maior = num  # Atualiza o maior número
    return maior

# Exemplo de uso da função
lista_numeros = [3, 7, 1, 9, 4, 5]
print(f"O maior número da lista é: {maior_numero(lista_numeros)}")
