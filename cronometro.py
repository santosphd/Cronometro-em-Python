# Cronômetro simples em Python
import time
import os

segundos = 0
minutos = 0
horas = 0
cronometro = ''

while True:
    # Limpa a tela
    os.system('clear')

    segundos += 1

    # Após 60 segundos, acrescenta 01 no campo minuto e zera o campo segundo
    if segundos >= 60:
        minutos += 1
        segundos = 0

    # Após 60 minutos, acrescenta 01 no campo hora e zera o campo minuto
    if minutos >= 60:
        horas += 1
        minutos = 0

    cronometro = (f'{horas:02d}:{minutos:02d}:{segundos:02d}')
    print('Cronômetro:')
    print(cronometro)
    
    # Aguarda 01 segundo antes de voltar ao começo do código
    time.sleep(1)
      


