# 14-celsius-farenheit.py = Escreva um programa que converta uma temperatura
# digitada em °C em °F.
# A fórmula para essa conversão ée: 
# F = (C * 9/5) + 32

celsius = float(input("Digite a temperatura em °C:"))
farenheit = 9 * celsius / 5 + 32
print(f"{celsius:.2f}°C é igual a {farenheit:.2f}°F")