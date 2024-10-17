# Solicita ao usuário para inserir um número
# Camila Queiroz 2°C

numero = int(input("Digite um número para ver a tabuada: "))

# Exibe a tabuada do número
print(f"Tabuada de {numero}:")
for i in range(1, 11):  # De 1 a 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")