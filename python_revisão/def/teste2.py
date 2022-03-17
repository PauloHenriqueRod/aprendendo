from inspect import BoundArguments


def turma(*num, situação = False):
    dic = dict()
    dic['Maior Nota'] = max(num)
    dic['Menor Nota'] = min(num)
    média = sum(num)/len(num)
    dic['Media'] = f'{média:.2f}'
    if situação:
        if média > 7:
            dic['Situação'] = 'Boa'
        elif média < 5:
            dic['Situação'] = 'Ruim'
        else:
            dic['Situação'] = 'Razoável'
    return dic

n = turma(7, 5, 7, 8, situação=True)
for c, d in n.items():
    print(f'{c}: {d}')
    