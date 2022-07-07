# hora_saida = int(input('Digite a hora de saída: '))
# minuto_saida = int(input('DIgite o minuto de saída: '))

# minuto_chegada = minuto_saida + 15
# hora_chegada = hora_saida

# if minuto_chegada > 59:
#      minuto_chegada -= 60
#      hora_chegada +=1

# if hora_chegada > 23:
#      hora_chegada -= 24

     
# print(f'Saída: {hora_saida:02}:{minuto_saida} | Chegada: {hora_chegada:02}:{minuto_chegada:02}')



verdadeiro = True
falso = False

print(bool(1))
print(bool(0))
print(bool(10))
print(bool(-10))
print(bool(10.23))
print(bool(0.23))
print(bool('a'))
print(bool('0'))
print(bool(''))

valor = ''

if not valor: #false
     print('Você não digitou um valor')

if valor == '':
     print('Voce nao digitou nengum valor')
     