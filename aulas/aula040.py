while True:
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    operador = input('Digite o operador(+ - / *): ')
    while operador not in '+-/*':
        print('não reconheci o operador, tente novamente')
        operador = input('Digite o operador(+ - / *): ')
    if operador == '+':
        print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')
    elif operador == '-':
        print(f'{numero_1} - {numero_2} = {numero_1 - numero_2}')
    elif operador == '*':
        print(f'{numero_1} * {numero_2} = {numero_1 * numero_2}')
    elif operador == '/':
        print(f'{numero_1} / {numero_2} = {numero_1 / numero_2}')
    prosseguir = input('Quer continuar? [S/N] ').upper()
    while prosseguir not in 'SN':
        print('DIGITE [S]im OU [N]ão')
        prosseguir = input('Quer continuar? [S/N] ').upper()
    if prosseguir == 'N':
        break
print('fim')
