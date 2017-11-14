#10º Desafio: Escreva um programa que leia quanto dinheiro tem na carteira e converta para dolar
print('========DESAFIO10========')

valor = float(input('Digite quanto dinheiro deseja converter: '))
dolar = valor/3.27

print('R${:.2f} REAL convertido para ${:.2f} DOLARES.'.format(valor, dolar))
