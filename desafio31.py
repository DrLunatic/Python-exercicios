#31º Desafio: Programa que pergunte a distância de uma viagem em km
#Calcule o preço da passagem, cobrando R$0,50 por Km, para viagens de até 200km
#e R$0,45 para viagens mais longas  .
print('========DESAFIO31========')

distancia = int(input('Insira a distância em km: '))

passagem_normal = 0.50
passagem_longa = 0.45

if(distancia <= 200):
    print('O valor da passagem é R${:.2f}'.format(distancia*passagem_normal))
else:
    print('O valor da passagem é R${:.2f}'.format(distancia*passagem_longa))