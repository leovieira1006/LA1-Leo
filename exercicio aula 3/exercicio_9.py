# Escreva um script que receba três valores A, B, C. Faça as comparações necessárias para exibir na tela o maior valor entre os três.

# Exemplo 01
# Entrada:
# 10
# 12
# 2
# Saída:
# O maior número é 12

# Exemplo 02
# Entrada:
# 12
# 2
# 10
# Saída:
# O maior número é 12

# Exemplo 03
# Entrada:
# 2
# 10
# 12
# Saída:
# O maior número é 12

a = 2
b = 10
c = 11

if a > b and a > c:
    print(f'O maior número sera {a}')

elif b > c:
    print(f'O maior número sera {b}')

else:
    print(f'O maior número sera {c}')
