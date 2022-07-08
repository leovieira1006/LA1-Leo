# Leia o salario de um trabalhador e o valor da prestação de um empréstimo. 
# Se a prestaçao for maior que 20% do salário imprima: “empréstimo não concedido”,
#  caso contrario imprima: “empréstimo concedido”.

salario = float(input('DIgite o salario do funcionario: '))
valor_prestacao = float(input('DIgite o valor da prestação: '))

porcentagem_salario = salario * .2

if valor_prestacao < porcentagem_salario:
    print('Emprestimo concedido')
else:
    print('Emprestimo não concedido')

