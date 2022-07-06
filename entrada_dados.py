name = input('Digite um nome: ')    #entrada de dados (pedir para digitar algo)
print(name)                         # vai mostrar o que foi digitado

#entrada de dados
valor_a = int(input('digite o valor A: '))     # trasformar de str para int
valor_b = int(input('digite o valor B: '))

#processamento
soma = valor_a + valor_b

#saida de dados
print(soma)

nasceu = int(input('digite o ano que nasceu: '))
ano = int(input('Digite o ano atual: '))
idade = ano - nasceu
print(f'Sua idade é: {idade}')