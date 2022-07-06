'''
Regras de nomenclatura de vaiaveis:

- Não pode usar simbolo ou numero na frente (exceto _)
- Cada palavra deve ser separada por _.
- Os nomes das variaveis devem ser descritos.
'''

# Colocar varias variaveis com o mesmo nome sempre vai mostrar o da ultima linha



name = 'Leonardo' #str
vazio = None #nonetype
numero_inteiro = 250 #int
numero_decimal = 10.1 #float
presente = True #boot

# contas: a unica operação que ira fazer é a multiplicação, que vaimostra a palavra o numero de vezes que eu colocar



print(f'o meu nome é {name}')
print(vazio)
print(numero_inteiro)
print(numero_decimal)
print(presente)

#Mostra  o tipo da vairavel

# print(type(name))
# print(type(vazio))
# print(type(numero_inteiro))
# print(type(numero_decimal))
# print(type(presente))

# Varias variaveis na mesma linha é confuso. Só se usa para trocar valores de variaveis

a, b, c = 1, 2, 3 # COnfuso, nao fazer

a = 10 # a = 10, b = none, aux = none
b = 5 # a = 10, b = 5, aux = none
aux = a # a = 10, b = 5, aux = 10
a = b # a = 5, b = 5, aux = 10
b = aux # a = 5, b = 10, aux = 10
print(a, b)

c = 10
d = 5
c, d = d, c
print(c, d)

valor_com_muitas_casas_decimais = 10.56465151561
print(f'o valor formatado é: {valor_com_muitas_casas_decimais:.2f}')