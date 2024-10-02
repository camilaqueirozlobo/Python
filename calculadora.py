def calcular(opcao, num1, num2):
    if opcao == 1:
        return num1 + num2
    elif opcao == 2:
        return num1 - num2
    elif opcao == 3:
        return num1 * num2
    elif opcao == 4:
        return num1 / num2 if num2 != 0 else "Erro: Divisão por zero não é permitida."
    elif opcao == 5:
        return num1 % num2 if num2 != 0 else "Erro: Divisão por zero não é permitida."
    else:
        return "Opção inválida."

def inicio():
    operacoes = {
        1: "soma",
        2: "subtração",
        3: "multiplicação",
        4: "divisão",
        5: "resto da divisão",
        6: "sair"
    }

    while True:
        print("## CALCULADORA ##\n")
        for chave, valor in operacoes.items():
            print(f"{chave}. {valor}")

        opcao = int(input("Digite uma opção: "))
        
        if opcao in operacoes and opcao != 6:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            resultado = calcular(opcao, num1, num2)
            print(f"O resultado da operação é: {resultado}\n")
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

inicio()