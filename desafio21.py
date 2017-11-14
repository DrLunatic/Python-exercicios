#21º Desafio: Tocando mp3 no python
from pygame import mixer
print('========DESAFIO21========')
mixer.init()
mixer.music.load('xa.mp3')
mixer.music.play()


decisao = (1)

while(decisao==1):
    decisao = int(input('1 Para continuar 2 Para parar'))
    if(decisao==2):
        mixer.music.stop()
        break
    else:
        print('musica continua')