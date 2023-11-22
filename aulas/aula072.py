# Multiplicação
def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

mult = multiplicacao(5,2,3,4,5,6)
print(mult)
print(5*2*3*4*5*6)

def par_impar(numero):
    mult_2 = numero % 2 == 0

    if mult_2:
        return f'{numero} é par'
    return f'{numero} é ímpar'

# Par ou Ímpar   
print(par_impar(10))




