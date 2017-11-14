#27º Desafio: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
print('========DESAFIO27========')

n = str(input('Insira o seu nome completo: ')).strip()

nome = n.split()

print('O Primeiro nome é: {}'.format(nome[0]))
print('O Segundo nome é: {}'.format(nome[len(nome) - 1]))
