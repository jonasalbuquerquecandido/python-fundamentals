# Crie um programa em Python que peça números ao usuário e calcule a soma total. O programa deve continuar pedindo novos números até que o usuário digite 0, momento em que a execução será encerrada e o resultado, exibido.

soma = 0
while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))
    if numero == 0:
        break
    soma += numero

print("A soma total é:", soma)