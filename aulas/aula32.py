"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)    
    if numero_int % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')
except:
    print('O número informado não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas =(input('Que horas são? '))
try:
    horas_int = int(horas)
    if horas_int >= 0 and horas_int <= 11:
        print('Bom dia')
    if horas_int >= 12 and horas_int <= 17:
        print('Boa tarde')
    if horas_int >= 18 and horas_int <= 23:
        print('Boa noite')
    else:
        print('Você digitou um horário inválido')
except:
    print('Por favor, digite apenas números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)
if nome:
    if tamanho_nome <=4:
        print('"Seu nome é curto"')
    elif tamanho_nome <=6:
        print('"Seu nome é normal"')
    elif tamanho_nome >6:
        print("Seu nome é muito grande")
else:
    print('Por favor, digite alguma coisa')
 
 