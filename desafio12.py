#12º Desafio: Receber um valor e dar 5% de desconto
print('========DESAFIO12========')

valor = float(input('Insira o valor do produto: '))

print('Valor do produto :R${}'.format(valor))
print('Valor do produto com desconto:R${}'.format(valor - ( valor * 5 ) / 100))
print('Valor do desconto: R${}'.format( (valor*5)/100))