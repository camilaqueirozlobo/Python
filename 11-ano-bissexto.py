# Função para verificar se um ano é bissexto
def verificar_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Solicitar ao usuário que insira um ano
try:
    ano = int(input("Digite um ano: "))
    if verificar_ano_bissexto(ano):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")
except ValueError:
    print("Por favor, insira um ano válido.")