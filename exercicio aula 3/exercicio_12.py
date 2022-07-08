# Leia um número fornecido pelo usuário.
#  Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, 
#  mostre uma mensagem dizendo que o número é inválido.

numero = int(input('DIgite um valor a ser calculado: '))

if numero > 0:
    print(numero ** 2)
else:
    print('numero invalido!')