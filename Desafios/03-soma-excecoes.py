# Desafio: Soma de Números com Tratamento de Exceções
soma = 0
while True:
    try:
        numero = int(input("Digite um número (ou 0 para encerrar): "))
        if numero == 0:
            break
        soma += numero
    except ValueError:
        print("Por favor, digite um número válido.")

print("A soma total é:", soma)