
def  processar_valor():
    valor = float(input('digite um valor: '))

    if valor < 0:
        print('O modulo do valor é: {} ' .format(abs(valor)))
    elif valor > 10:
        outro_valor = float(input('Digite outro valor: '))
        diferença = valor - outro_valor
        print('A diferença entre os valores é: {}'.format(diferença))
    else:
        resultado = valor / 5
        print('O valor dividido por 5 é {}'.format(resultado))

print('='*50)
print('NOME: Matheus Henrique de Campos Rumão ')
print('RA: 1051392421015 ')
print('='*50)
processar_valor()