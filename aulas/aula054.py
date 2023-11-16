"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistente na lista
"""
import os

valores = []
while True:
    print('Selecione um opção')
    escolha = input('[i]nserir [a]pagar [l]istar: ').lower()
    if escolha == 'i':
        os.system('cls')
        valor = input('Valor: ')
        if valor not in valores:
            valores.append(valor)
    
    elif escolha == 'a':
        apagar = input('Escolha o índice para apagar: ')
        try:
            apagar_int = int(apagar)
            del valores[apagar_int]
        except ValueError:
            print('Por favor, digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista')

    elif escolha == 'l':
        os.system('cls')
        if valores == []:
            print('"A lista está vazia"')
        else:    
            for indice, nome in enumerate(valores):
                print(indice, nome)
    else:
        print('Escolha inválida!')
