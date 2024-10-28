def acrescimo_20(salario):
    acrescimo = salario + (salario * 0.20)
    return acrescimo
def acrescimo_10(salario):
    acrescimo = salario + (salario * 0.10)
    return acrescimo
def acrescimo_5(salario):
    acrescimo = salario + (salario * 0.05)
    return acrescimo


print('='*50)
print('NOME: Matheus Henrique de Campos Rumão ')
print('RA: 1051392421015 ')
print('='*50)

salario = float(input('Qual seu salário: '))   

if salario <= 1500:
    print('Você teve aumento de 10% seu novo salário é R${:.2f}'.format(acrescimo_20(salario)))
elif salario > 1500 and salario < 2500:
    print('Você teve aumento de 10% seu novo salário éR${:.2f}'.format(acrescimo_10(salario)))
else:
    print('Você teve aumento de 5% seu novo salário éR${:.2f}'.format(acrescimo_5(salario)))