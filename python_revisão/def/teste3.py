from time import sleep
cores = ('\033[m'     # sem cores=0
     '\033[41m',  # vermelho=1
     '\033[42m',  # verde=2
     '\033[43m',  # amarelo=3
     '\033[44m',  # azul=4
     '\033[45m'   # magenta=5
     )


def ajuda(com):
    título(f'Acessando manual do comando \"{com}\"', 4)
    print(cores[3], end='')
    help(com)
    print(cores[0], end = '')


def título(msg, cor = 0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)
    print(cores[0], end='')
    sleep(1.5)


while True:
    título('Sistema de ajudas pyhel', 2)
    sleep(0.5)
    comando = str(input('FUNÇÃO OU BIBLIOTECA: '))
    if comando.upper() == 'FIM':
        break
    else:
        print(ajuda(comando))
print('\033[mFIM')
