#20º Desafio: Sortear ordem dos alunos para apagar o quadro
import math
import random
print('========DESAFIO20========')

alunos = ['Fernando', 'Lucas', 'Gustavo', 'Elaine']

random.shuffle(alunos)

print('Ordem de apresentação é: {}'.format(alunos))