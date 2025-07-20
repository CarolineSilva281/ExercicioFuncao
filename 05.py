# Função para classificar o horário do dia
def saudacao_por_hora():
    # Pede para o usuário digitar a hora (0 a 23)
    hora = int(input("Digite a hora (0 a 23): ")) 
    
    # Usa condicional para verificar o período do dia
    if 5 <= hora < 12:
        print("Bom dia!")
    elif 12 <= hora < 19:
        print("Boa tarde!")
    else:
        print("Boa noite!")

# Chamando a função
saudacao_por_hora()
