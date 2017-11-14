#17º Desafio: Programa que leia o omprimento do cateto oposto e cateto adjacente de um triangulo
#retangulo, calcule e mostre o comprimento da hipotenuza
import math
print('========DESAFIO17========')

cato = float(input('Cateto Oposto: '))
cata = float(input('Cateto Adjacente: '))


resposta = math.hypot(cato, cata)

print('Comprimento da Hipotenuza é igual a : {:.2f}'.format(resposta))