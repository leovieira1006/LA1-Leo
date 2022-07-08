turno = input('Digite seu horario (M - matutino | V - vespertino | N - noturno').upper # mostra qualquer letra em maiusculo (capslock)

if turno == 'M':
    print('Bom dia ')
elif turno == 'V':
    print('Boa tarde')
elif turno == 'N':
    print('Boa noite')
else:
    print('valor invalido')
