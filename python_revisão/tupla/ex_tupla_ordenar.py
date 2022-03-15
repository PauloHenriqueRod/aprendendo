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

# ----------------- OUTRO MODO DE FAZER -----------------

# from random import randint
# from time import sleep
# pos = 1
# jog = {'Jogador 1': randint(1,6),
#      'Jogador 2': randint(1,6),
#      'Jogador 3': randint(1,6),
#      'Jogador 4': randint(1,6)}
# for k, v in jog.items():
#     print(f'O {k} tirou {v}')
#     sleep(0.8)
# b = sorted(jog, key=jog.get, reverse=True)
# for i in sorted(jog,key=jog.get,reverse=True):
#     print(f'{pos}º- {i}: tirou {jog[i]}')
#     pos += 1