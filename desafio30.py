#30º Desafio: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
import math
print('========DESAFIO30========')

num = int(input('Digite um número: '))

if((num) % 2 == 0):
    print('O número {} é par'.format(num))
else:
    print('O número {} digitado é impar.'.format(num))