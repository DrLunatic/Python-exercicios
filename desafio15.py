#15º Desafio: Converter Celcius pra Fahrenheit
print('========DESAFIO15========')

dias = int(input('Digite a quantidade de dias de aluguel: '))
kmr = int(input('Digite a quantidade de km rodados: '))

vldia = 60
vlkmr = 0.15

total = (dias*vldia)+(kmr*vlkmr)

print('Valor total a ser pago é: R${:.2f}'.format(total))