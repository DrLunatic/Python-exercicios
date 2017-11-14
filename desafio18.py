#18º Desafio: Faça um program que leia um angulo e mostra o seno, cosseno e tangente
import math
print('========DESAFIO18========')
angulo = int(input('Insira o ângulo'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor do seno: {:.2f}\ncosseno: {:.2f}\nTangente: {:.2f}'.format(seno, cosseno, tangente))