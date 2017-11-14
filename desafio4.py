#4ºDesafio fazer um programa que leia algo e mostre todas as informações possiveis usando o "is"

print('========DESAFIO4========')

algo = input('Digite qualquer coisa!: ')

print('O Valor é?')
print('Numérico?: ', algo.isnumeric())
print('Alfanumérico?: ', algo.isalnum())
print('É um espaço?: ', algo.isspace())
print('É minusculo?: ', algo.islower())