#26º Desafio:Faça um programa que leia uma frase pelo teclado e mostr:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primera vez
#Em que posição ela aparece a última vez.
print('========DESAFIO26========')

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frae.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
