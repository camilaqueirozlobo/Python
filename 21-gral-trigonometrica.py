import math

def graus_para_radianos(graus):
    return graus * (math.pi / 180)

def radianos_para_graus(radianos):
    return radianos * (180 / math.pi)

def calculadora_trigonometro():
    print("Calculadora Trigonométrica")
    print("1. Converter graus para radianos")
    print("2. Converter radianos para graus")
    
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == '1':
        graus = float(input("Digite o ângulo em graus: "))
        radianos = graus_para_radianos(graus)
        print(f"{graus} graus é igual a {radianos} radianos.")
        
    elif escolha == '2':
        radianos = float(input("Digite o ângulo em radianos: "))
        graus = radianos_para_graus(radianos)
        print(f"{radianos} radianos é igual a {graus} graus.")
        
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora_trigonometro()