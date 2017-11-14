#8º Desafio: Escreva um programa que leia um valor em metros e exiba em centimetros e milimetros
print('========DESAFIO8========')

medida = int(input('Digite o valor em metros: '))
km = medida /1000
hm = medida / 100
dam = medida / 10
dm = medida*10
cm = medida * 100
mm = medida * 1000

print('Conversão de metros para outros valores:')
print('km: {}\nhm: {}\ndam: {}\ndm: {}\ncm: {}\nmm: {}'.format(km, hm, dam, dm, cm, mm))
