#11º Desafio: Programa ue leia a largura e a altura de uma parede em metros,
#calcule a sua área de a quantidade de tinta necessária para pinta-la sabendo
# que cada litro de tina pinta 2m²
print('========DESAFIO11========')

largura = int(input('Insira a altura em metros: '))
altura = int(input('Insira a largura em metros: '))
area = largura * altura

print('Sa parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))

tinta = area /2

print('Para pintar essa parede, voce precisará de {}l de tinta.'.format(tinta))