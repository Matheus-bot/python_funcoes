def calcular_media(n1, n2 ):
    return (n1 + n2) / 2

print('='*50)
print('NOME: Matheus Henrique de Campos Rumão ')
print('RA: 1051392421015 ')
print('='*50)

nome = input('NOME: ')
ra = int(input('RA: '))
print('='* 30 )
n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))

media = calcular_media(n1, n2)
print('Sua média foi: ', media)


if media >= 7:
    print('Parabéns, Você está aprovado ')
elif  media < 5:  
    print('Você ainda tem uma chance! estude mais para o exame ')
    print('='*30)
    exame = int(input('Qual nota você tirou no exame?'))
            
    if exame >= 5:
        print('Parabéns, você aproveitou a sua chance, Está aprovado!!! ')
    elif exame < 5:
        print('Estude mais para a próxima. Você não alcançou o mínimo necessário')

print('='*30)

