#33º Desafio: Programa que leia três números e mostre qual é o maior e qual é o menor
print('========DESAFIO33========')

n1 = int(input('Insira o primeiro número'))
n2 = int(input('Insira o segundo número'))
n3 = int(input('Insira o terceiro número'))

menor = n1
maior = n1
#Verifica o menor
if n2 < n1 and n2 < n3:
    menor = n2
if n2 < n1 and n3 < n2:
    menor = n3
#Verifica o maior
if n2 > n1 and n2 > n3:
    maior = n2
if n2 > n1 and n3 > n2:
    maior = n3

print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))