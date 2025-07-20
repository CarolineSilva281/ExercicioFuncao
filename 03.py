# Função para mostrar a tabuada do 5
def tabuada():
    # Laço para multiplicar 5 por cada número de 1 a 10
    for i in range(1, 11):  # A função range(1, 11) gera números de 1 a 10
        resultado = 5 * i  # Multiplica 5 pelo número atual
        print(f"5 x {i} = {resultado}")  # Exibe o resultado da multiplicação

# Chamando a função
tabuada()
