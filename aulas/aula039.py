"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

cont = 0
novo_nome = ''

while cont != len(nome):
    letra = nome[cont]
    novo_nome += f'!{letra}'
    cont += 1

novo_nome += '!'
print(novo_nome)