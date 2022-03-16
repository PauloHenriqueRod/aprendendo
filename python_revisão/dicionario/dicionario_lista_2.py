jogadores = []
while True:
    jogador = dict()
    gols = []
    cont = 0
    jogador['Nome'] = str(input('Nome do jogador: '))
    n = int(input('Quantas partidas jogou? '))
    jogador['Jogos'] = n
    for c in range(0, n):
        g = int(input(f'Quantos gols na partida {c+1} '))
        gols += [g]
        cont += g
    jogador['Gols'] = gols
    jogador['Total de gols'] = cont
    jogadores.append(jogador.copy())
    b = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while b not in 'SN':
        b = str(input('Reponda apenas SN')).strip().upper()
    if b == 'N':
        break
print()
print('  {:<15}{:^30}{:^60}'.format('NOME:', 'GOLS', 'TOTAL'))
for c in range(0, len(jogadores)):
    print('{} {:<15}{!s:^30s}{:^60}'.format(c+1, jogadores[c]['Nome'], jogadores[c]['Gols'],
                                            jogadores[c]['Total de gols']))
print('-='*50)
while True:
    n = int(input('Dados de qual jogador? '))
    if n == 999:
        break
    if n > len(jogadores):
        print('Jogador não registrado')
    else:
        print('Jogador: {}'.format(jogadores[n - 1]['Nome']))
        for d in range(0, jogadores[n-1]['Jogos']):
            print('Jogo {} {} gols'.format(d+1, jogadores[n-1]['Gols'][d]))
