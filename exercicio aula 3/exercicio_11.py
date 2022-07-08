# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno. Sendo que:

# Triângulo Equilátero: possui os 3 lados iguais.
# Triângulo Isósceles: possui 2 lados iguais.
# Triângulo Escaleno: possui 3 lados diferentes.

lado_a = int(input('Digite o primeiro lado: '))
lado_b = int(input('Digite o segundo lado: '))
lado_c = int(input('Digite o terceiro lado: '))

if lado_a == lado_b and lado_b == lado_c:
    print('O triangulo é equilátero')
elif lado_a != lado_b and lado_b != lado_c:
    print('O triangulo é escaleno')
else:
    print('O triangulo é isósceles')
