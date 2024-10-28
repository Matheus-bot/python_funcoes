def calcular_media(n1, n2 ):
    return (n1 + n2) / 2

print('='*50)
print('NOME: Matheus Henrique de Campos Rumão ')
print('RA: 1051392421015 ')
print('='*50)

nome = input('NOME: ')
ra = int(input('RA: '))
n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))

media = calcular_media(n1, n2)
print('Sua média foi: ', media)

if media >= 7:
    print('Parabéns, Você está aprovado ')
elif  media < 5:  
    print('Você ainda tem uma chance! estude mais para o exame ')
