#29º Desafio: Faça um programa que leia a velocidade de um carro, se ele ultrapassar 80km
#mostre uma mensagem dizendo que ele foi multado, a multa vai custar R$7.00 por cada Km acima do limite.
print('========DESAFIO29========')

km = int(input('Digite a velocidade: '))
multa = 7
limitekm = 80
if(km>limitekm):
    print('Você está acima da velocidae permitida!\nVocê foi multado!')
    print('Você foi multado em R${:.2f}'.format((km-limitekm)*multa))
else:
    print('Você não foi multado!')