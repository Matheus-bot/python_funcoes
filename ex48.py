def calculo_idade(idade):
    if (idade > 18) and  (idade < 65):
        print('Você é maior de idade ')
    elif (idade > 65):
        print('Você é maior de 65 anos ')
    else:
        print('Você é menor de idade')
  
print('='*50)
print('NOME: Matheus Henrique de Campos Rumão ')
print('RA: 1051392421015 ')
print('='*50)

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

print('Bem vindo {}'.format(nome), end=' ')
calculo_idade(idade)