#6º Desafio: Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada
print('========DESAFIO6========')

valor = float(input('Digite o valor desejado: '))

print('Dobro do valor: {}\nSeu triplo: {}'.format(valor*2, valor*3))
print('Raiz do valor: {:.2f}'.format(valor**(1/2)))