# Gerador de números aleatórios
import random
print("=" * 40)
print("GERADOR DE NÚMEROS DA SORTE")
print("=" * 40) 
nome = input("\nQual é o seu nome? ")
mes = int(input("Em qual mês você nasceu? (1-12) "))
dia = int(input("Em qual dia você nasceu? (1-31) "))
numeros_sorte = random.sample(range(1, 60), 6)
numero_especial = (mes+dia) % 10
print("\n" + "-" * 40)
print(f"Olám {nome}!")
print(f"Seus números da sorte são: {numeros_sorte} e o número especial é: {numero_especial}")
print("-" * 40)