matriz = [[], [], []]
for d in range(0, 3):
    for c in range(0, 3):
        while True:
            try:
                n = int(input(f'DIGITE UM NÚMERO PARA A POSIÇÃO [{d+1}, {c+1}]'))
                matriz [d] += [n]
                break
            except:
                print('VALOR INVÁLIDO')
for e in matriz:
    print(e)
d1 = 1
for c in range(0, 3):
    d1 *= matriz[c][c]
d2 = matriz[2][0]
for c in range(0, 2):
    d2 *= matriz[c][c+1]
d3 = matriz[0][2]
for c in range(0, 2):
    d3 *= matriz[c+1][c]
d4 = matriz[0][2]*matriz[1][1]*matriz[2][0]
d5 = matriz[2][1]*matriz[1][2]*matriz[0][0]
d6 = matriz[2][2]*matriz[1][0]*matriz[0][1]
print(f'\nDETERMINANTE: {(d1+d2+d3)-(d4+d5+d6)}')
