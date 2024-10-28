def desconto_20(n):
    desconto = n - (n * 0.20)
    return desconto

def desconto_10(n):
    desconto = n - (n * 0.10)
    return desconto

def desconto_5(n):
    desconto = n - (n * 0.05)
    return desconto 

print('='*50)
print('NOME: Matheus Henrique de Campos Rumão ')
print('RA: 1051392421015 ')
print('='*50)
print('='*30)
print('BEM VINDO A NOSSA LOJA')
print('='*30)
total = float(input('Qual o valor da compra ?'))

if total > 300:
    print('Você ganhou desconto de 20%, de R${:.2f} ficou R${:.2f} '.format((total), desconto_20(total)))
elif (total > 200) and (total < 299): 
    print('Você ganhou desconto de 10%, de R${:.2f} ficou R${:.2f} '.format((total), desconto_10(total)))
elif total < 199:
    print('Você ganhou desconto de 5%, de R${:.2f} ficou R${:.2f} '.format((total), desconto_5(total)))
