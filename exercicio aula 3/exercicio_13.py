# Escreva um script para ler um número e informar se ele é divisível por 5.

numero = int(input('Digite um número: '))
calculo = (numero % 5)

if calculo == 0:
    print('o numero é divisivel por 5')
else:
    print('O numero não é divisivel por 5')