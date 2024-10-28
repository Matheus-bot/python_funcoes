def divisivel_por_dez(n1):
    if n1 % 10 == 0 :
        print('Divisivél por 10 ')
    else:
        print('O valor não é divisível por 10')

def divisivel_por_cinco(n1):
    if n1 % 5 == 0 :
        print('Divisivél por 5 ')
    else:
        print('O valor não é divisível por 5')

def divisivel_por_dois(n1):
    if n1 % 2 == 0 :
        print('Divisivél por 2 ')
    else:
        print('O valor não é divisível por 2')

print('='*50)
print('NOME: Matheus Henrique de Campos Rumão ')
print('RA: 1051392421015 ')
print('='*50)

num = int(input('digite um valor: '))
divisivel_por_dez(num)
divisivel_por_cinco(num)
divisivel_por_dois(num)