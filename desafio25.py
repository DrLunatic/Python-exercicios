#25º Desafio: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print('========DESAFIO25========')

nome = str(input('Insira o seu nome ocmpleto: ')).strip()

print('Seu nome tem Silva? {}.'.format('SILVA' in nome.upper()))