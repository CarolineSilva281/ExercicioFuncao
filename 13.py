# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32  # Fórmula de conversão
    return fahrenheit

# Solicitando a temperatura em Celsius ao usuário
temp_celsius = float(input("Digite a temperatura em Celsius: "))

# Exibindo a conversão
print(f"A temperatura em Fahrenheit é: {celsius_para_fahrenheit(temp_celsius)}°F")
