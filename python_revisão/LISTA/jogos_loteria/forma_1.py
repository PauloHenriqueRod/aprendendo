from random import randint
from time import sleep

lista = []
jogos = []
quant = int(input('QUANTIDADE DE JOGOS: '))
tot = 1
for c in range(0, quant):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista += [num]
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
for i, c in enumerate(jogos):
    print(f'JOGO {i+1}: {c}')
    sleep(0.75)
