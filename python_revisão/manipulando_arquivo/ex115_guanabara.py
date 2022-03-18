from pacote_115 import *
from time import sleep


while True:
    resposta = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVAS PESSOAS', 'SAIR DO SISTEMA'])
    if resposta == 1:
        cabeçalho('OPÇÃO 1')
        with open('cadastros.txt', 'r') as arquivo:
            lista = arquivo.read()
            print(lista)
            arquivo.close()
    elif resposta == 2:
        cabeçalho('OPÇÃO 2')
        nome = str(input('NOME: '))
        idade = int(input('IDADE: '))
        with open('cadastros.txt', 'a+') as arquivo:
            arquivo.write(f'\n{nome} - {idade}')
            arquivo.close()
    elif resposta == 3:
        break
    else:
        print('DIGITE UMA OPÇÃO VÁLIDA')
