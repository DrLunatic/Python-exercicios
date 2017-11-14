#34º Desafio: Programa que pergunte o salário de um funcion´rio e calcule o valor do seu aumento
#Para salario superiores a R$1.250.00 aumento e 10%, para salarios inferiores o aumento é de 15%
print('========DESAFIO34========')

salario = float(input('Insira o valor do salário: '))

if(salario < 1250):
    print('Salário atual R${:.2f}\nSalário com aumento R${:.2f}'.format(salario, salario + (salario * 15 / 100)))
else:
    print('Salário atual R${:.2f}\nSalário com aumento R${:.2f}'.format(salario, salario + (salario * 10 / 100)))