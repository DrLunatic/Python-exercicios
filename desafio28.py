#28º Desafio: Faça o computador "pensar" em um número inteiro entre 0 e 5 para o usuario tentar
#descobrir qual foi o numero escolhido, o programa devera escrever na tela se o usuario acertou .
print('========DESAFIO28========')
import random
from time import sleep

num = random.randrange(0 ,5)

numero = int(input('Insira um numero entre 0 a 5: '))

print('Processando.')
sleep(1)
print('Processando..')
sleep(1)
print('Processando...')
sleep(1)

if(numero==num):
    print('Você acertou!')
else:
    print('Você errou! O número certo é: {}'.format(num))