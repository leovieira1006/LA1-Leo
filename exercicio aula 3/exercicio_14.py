# Leia um número. Se o número for positivo imprima a raiz quadrada desse número. Do contrário, imprima o número ao quadrado.

numero = int(input('Digite um numero: '))

positivo = (numero ** (1/2))
negativo = (numero ** 2)

if numero > 0:
    print(positivo)
else:
    print(negativo)
