#Elaborar um algoritmo que solicita 4 notas ao usuário.
#o programa de calcular de calcular a média das notas e
#verificar se a media é maior ou igual a a 80, o programa 
#Deve exibir a mensagem "aprovado" e se a média for menor que 
#80, o programa deve exibir a mensagem "reprovado"

nota1 = float(input("digite a nota1:"))
nota2 = float(input("digite a nota2:"))
nota3= float(input("digite a nota3:"))
nota4 = float(input("digite a nota4:"))

media = (nota1 + nota2 + nota3 + nota4) / 4 
print(f"a média final obtida = {media}")

if (media >= 80):
    print("aprovado")
else:
    print("reprovado")
