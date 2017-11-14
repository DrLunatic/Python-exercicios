#16º Desafio: Ler um número real e mostrar apenas sua parte inteira
import math
print('========DESAFIO16========')
num = float(input('Digite um numero com casas decimais: '))


print('A parte inteira de {} é: {}'.format(num, math.floor(num)))