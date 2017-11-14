#22º Desafio: Programa para ler um nome completo e mostrar
#O nome com todas as letras maiúsculas
#Nome com todas as letras minúsculas
#Quantas letras no total sem considerar espaço
#Quantas letra tem o primeiro nome
print('========DESAFIO22========')

nome = input('Insira o nome: ')

print('{} - Nome com todas as letras maiúsculas.'.format(nome.upper()))
print('{} - Nome com todas letras minúsculas.'.format(nome.lower()))
print('{} - Letras sem considerar os espaços.'.format(len(nome) - nome.count(' ')))
print('{} - Primeiro nome.'.format(nome.find(' ')))