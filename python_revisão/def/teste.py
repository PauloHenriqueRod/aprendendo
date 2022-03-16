def fatorial(n=1, show=False):
    """
    --->CALCULA O FATORIAL DE UM NÚMERO<---
    :param n: Número que vai dá o fatorial
    :param show: Mostrar ou não o cálculo
    :return: Show = False
    """
    f = 1
    if show:
        for d in range(n, 0, -1):
            if d > 1:
                print(f'{d} x', end=' ')
            else:
                print(f'{d} =', end=' ')
    for c in range(n, 0, -1):
        f *= c
    print(f)


fatorial(8, True)
