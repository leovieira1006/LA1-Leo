# Faça um script que leia três números e mostre-os em ordem decrescente.

a = int(input('Digite o valor para A: '))
b = int(input('DIgite o valor para B: '))
c = int(input('Digite o valor para C: '))

if c > b:
    c, b = b, c

if b > a:
    b , a = a, b

if c > b:
    c, b = b, c

print( a, b, c)
