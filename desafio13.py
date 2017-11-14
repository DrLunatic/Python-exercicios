#13º Desafio: Receber um valor e dar 15% de aumento
print('========DESAFIO13========')

valor = float(input('Insira o valor do salário: '))

print('Valor do salário :R${:.2f}\nValor do salário com aumento:R${:.2f}\nValor do aumento: R${:.2f}'.format(valor, valor+(valor*15)/100, (valor*15)/100))