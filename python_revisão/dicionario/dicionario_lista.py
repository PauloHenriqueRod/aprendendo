lista = []
idade_total = 0
while True:
    pessoa = dict()
    pessoa['Nome'] = str(input('NOME: ')).strip()
    pessoa['Sexo'] = str(input('SEXO[M/F/NDA]: ')).upper().strip()
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input('Responda apenas M/F/NDA: ')).upper().strip()
    pessoa['Idade'] = int(input('IDADE: '))
    idade_total += pessoa['Idade']
    cont = str(input('Deseja continuar?[S/N]')).upper().strip()
    while cont not in 'SN':
        cont = str(input('Digite apenas S ou N')).strip().upper()
    lista.append(pessoa.copy())
    if cont == 'N':
        break
media = idade_total/len(lista)
print('-='*30)
print(f'Ao todos temos {len(lista)} pessoas cadastradas')
print('-='*30)
print(f'A média de idade é de {media} anos')
print('-='*30)
print('PESSOAS CADASTRADAS COM SEXO FEMININO:')
for c in range(0, len(lista)):
    if lista[c]['Sexo'] == 'F':
        print(lista[c]['Nome'])
print()
print('-='*30)
print('Lista de pessoas com idade acima da média:')
for d in range(0, len(lista)):
    if lista[d]['Idade'] > media:
        print(lista[d]['Nome'])
