# Função para multiplicação de dois números
def multiplicacao(a, b):
    return a * b  # Retorna o produto dos dois números

# Solicitando os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibindo o resultado
resultado = multiplicacao(num1, num2)
print(f"O resultado da multiplicação é: {resultado}")
