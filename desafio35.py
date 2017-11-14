#35º Desafio: Ler três comprimntos de retas e dizer ao usuário se els podem ou não formar um triangulo

print('========DESAFIO35========')

print('-=-' * 20)
print('Analisador de Triaãngulos')
print('-=-' * 20)
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar triângulo!')
else:
    print('Os seguimentos acima não podem formar um triângulo!')