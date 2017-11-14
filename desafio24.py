#24º Desafio: Faça um programa ue leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"
#
print('========DESAFIO24========')

cid = str(input('Em que cidade você nasceu?: ')).strip() # "STRIP" Tira os espaços

print(cid[:5].upper() == 'SANTO') # "UPPER" Transforma tudo em maiusculo