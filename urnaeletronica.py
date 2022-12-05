"""
Projeto para simular uma urna eletronica
"""
from time import sleep
from playsound import playsound

votos_Enzo = 0
votos_Valdecir = 0
total_de_votos = 0
total_de_pessoas = 10

while True:
    print('-' * 25)
    print('Total Enzo: ', votos_Enzo)
    print('Total Valdecir: ', votos_Valdecir)
    print('-' * 25)
    voto_unico = int(input('\nPARA ENZO VOTE 1\nPARA VALDECIR VOTE 2\n-->'))
    if voto_unico == 1:
        print('Computando voto...')
        playsound("urnaeletronica.mp3")
        sleep(1)
        votos_Enzo += 1
        total_de_votos += 1
    elif voto_unico == 2:
        print('Computando voto...')
        playsound("urnaeletronica.mp3")
        sleep(1)
        votos_Valdecir += 1
        total_de_votos += 1

    if total_de_votos == total_de_pessoas:
        print('Os votos estão sendo analisados...')
        sleep(2)
        print('Enzo: ', votos_Enzo)
        print('Valdecir: ', votos_Valdecir)
        break
