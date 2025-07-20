# Função para calcular a média de 3 notas
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3  # Calcula a média
    return media

# Solicitando as notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Exibindo a média
print(f"A média das notas é: {calcular_media(nota1, nota2, nota3)}")
