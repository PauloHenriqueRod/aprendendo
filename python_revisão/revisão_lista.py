lista = ['Fluminense', 'Flamengo', 'Vasco', 'Botafogo']

# FUNÇÃO len(lista) CONTA O NÚMERO DE ELEMENTOS DA LISTA
print(len(lista))
print('=-'*30)

# max(lista), min(lista) -> ENCONTRA O MAIOR VALOR DA LISTA
lista_numérica = [1, 8, 4, 7, 16, 3]
print(max(lista_numérica))
# NO CASO DE LISTA COM APENAS PALAVRAS, ENCONTRA O ÚLTIMO ITEM EM ORDEM ALFABÉTICA
print(max(lista))
print('=-'*30)

# lista.append -> ADICIONA UM ITEM NA LISTA
# lista.insert(pos, x) -> ADICIONA UM ITEM NA POSIÇÃO X
lista.append('Corinthians')
print(lista)
lista.insert(2, 'Corissabá')
print(lista)
print('=-'*30)

# FUNÇÃO lista.index ENCONTRA A POSIÇÃO DO ITEM ESCOLHIDO, EM CASO DE NÃO EXISTIR O ITEM NA LISTA RETORNA A POSIÇÃO "-1"
print(lista.index('Fluminense'))
print('=-'*30)

# FUNÇÃO lista.count CONTA O NÚMERO DE VEZES QUE UM CERTO ELEMENTO APARECE NA LISTA
print(lista.count('Fluminense'))

# COMO ATUALIZAR UMA LISTA EM UMA FUNÇÃO DE REPETIÇÃO
lista = []
lista_final = []
while True:
    cont = str(input('ADICIONAR NOME NA LISTA?[S/N]')).upper()
    if cont == 'N':
        break
    else:
        nome = str(input('Nome: '))
        idade = str(input('Idade: '))
        lista.append(nome)
        lista.append(idade)
        lista_final.append(lista[:])
        lista.clear()
print(lista_final)
