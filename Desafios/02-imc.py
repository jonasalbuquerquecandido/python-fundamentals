# Desafio: Cálculo do IMC
nome = input("Digite o seu nome:")
peso = float(input("Digite o seu peso em kg:"))
altura = float(input("Digite a sua altura em metros:"))
imc = peso / (altura**2)
if imc < 18.5:
    print(f"{nome}, seu IMC é {imc:.2f} e você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"{nome}, seu IMC é {imc:.2f} e você está com peso normal.")
elif 25 <= imc < 30:
    print(f"{nome}, seu IMC é {imc:.2f} e você está com sobrepeso.")
elif 30 <= imc < 35:
    print(f"{nome}, seu IMC é {imc:.2f} e você está com obesidade grau 1.")
elif 35 <= imc < 40:
    print(f"{nome}, seu IMC é {imc:.2f} e você está com obesidade grau 2.")
else:   
    print(f"{nome}, seu IMC é {imc:.2f} e você está com obesidade grau 3.")