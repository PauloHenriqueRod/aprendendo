# VOCÊ PODE USAR "*" QUANDO O NÚMERO DE PARÂMETROS É INDETERMINADO
# OS PARÂMETROS SÃO RETORNADOS COMO TUPLA
def teste(*args):
    print(f'Você digitou {len(args)} argumentos')
    print(f'A soma deu {sum(args)}')
    print(type(args))

teste(8, 7, 6, 5, 1, 2, 9, 6, 4)
print()
teste(5, 2, 1, 7)
print('-='*30)

# VOCÊ PODE USAR "*" PARA LEVAR UMA LISTA PARA OS PARÂMETROS
def volume(altura, largura, comprimento):
    volume = altura*largura*comprimento
    return volume

lista = [5, 9, 7]
calc = volume(*lista)
print(f'O volume é {calc}')
print('-='*30)

# VOCÊ PODE USAR "**" PARA PARÂMETROS FOREM OPCIONAIS, OS VALORES SERÃO AGRUPADOS EM UM DICIONÁRO, PORTANTO DEVE-SE ACOMPANHAR O VALOR DO PARÂMETRO COM O "NOME" DA CHAVE
def volume(**info):
    vol = info['profundidade']*info['largura']*info['comprimento']
    return vol, info
piscina = volume(profundidade=5, largura=7, comprimento=2)
print(piscina)
print('-='*30)

# CASO OS ARGUMENTOS JÁ ESTEJAM AGRUPADOS EM UM DICIONÁRIO, PODE-SE USAR "**" PARA SERVIR DE ARGUMENTOS PARA A FUNÇÃO
def piscina(prof, largura=4, comprimento=5):
    vol = prof*largura*comprimento
    return vol

infos = {'largura': 8, 'comprimento': 18}

volume = piscina(3, **infos)

print('O volume é: ', volume)
