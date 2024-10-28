def valor_ao_cubo(n1):
    return n1 ** 3


def fatorial(n, show=False):
    f = 1 
    for c in range (n, 0, -1):
        if show:
            print(f'{c} X ', end='')
        f *= c
    return f

def dividido_por_nove(n2):
    return n2 / 9 

print('='*50)
print('NOME: Matheus Henrique de Campos Rumão ')
print('RA: 1051392421015 ')
print('='*50)

numero = int(input('Digite um valor '))

if numero == 1 or numero == 2:
    print('{} ao cubo é {} ' .format((numero) , valor_ao_cubo(numero)) )
elif numero % 3 == 0:
    resultado = fatorial(numero, show=True)
    print('O fatorial de {} é {}'.format((numero), fatorial(numero)))
elif numero in [4, 5, 7, 8]:
    print('{} dividido por 9 é {:.2f}'.format((numero), dividido_por_nove(numero)))
else:
    print('Valor inválido')