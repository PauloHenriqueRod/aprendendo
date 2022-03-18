def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUSURAIO NÃO DIGITOU UM NÚMERO')
            return 0
        else:
            return numero


def linha(tam = 42):
    return '-'*tam


def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRIINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leia_int('\033[32mSua opção: \033[m')
    return opc
