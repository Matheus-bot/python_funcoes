def elevado_ao_quadrado(valor):
    return valor ** 2

def raiz_quadrada(valor):
    return valor / 0.5

def divisao_por_nove(valor):
    return valor / 9

print('='*50)
print('NOME: Matheus Henrique de Campos Rumão: ')
print('RA: 1051392421015 ')
print('='*50)
valor = int(input('Digite um valor: '))

if valor in [1, 2, 3]:
    resultado = elevado_ao_quadrado(valor)
    print('O valor ao quadrado é: ', resultado)
elif (valor == 4) or (valor == 9):
    resultado = raiz_quadrada(valor)
    print('A Raiz quadrada desse numero é: ', resultado)
elif valor in [6, 7, 8]:
    resultado = divisao_por_nove(valor)
    print('Esse numero dividido por nove é: {:.2f} ' .format(resultado))
else:
    print('Esse valor não se encaixa nas operações')