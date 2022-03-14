from random import sample
from time import sleep

n = int(input('QUANTIDADE DE JOGOS: '))
jogos = [sample(range(1, 61), k=6)for x in range(0, n)]
for x, y in enumerate(jogos):
    print(f'JOGO {x + 1}: {sorted(y)}')
    sleep(0.6)
