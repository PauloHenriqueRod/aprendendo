from random import randint
from operator import itemgetter
from time import sleep

jogos = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1,6),
'Jogador 4': randint(1,6), 'Jogador 5': randint(1, 6)}

for c, v in jogos.items():
    print(f'{c} tirou {v}')
    sleep(0.8)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for q, r in enumerate(ranking):
    print(f'{q+1}º lugar - {r[0]} - {r[1]}')
    sleep(0.5)
