import csv
header = ['Nome', 'Gênero', 'Idade']
dados = []
opcao = int(input('1-ADICIONAR PESSOA\n2-SAIR DO PROGRAMA\n'))
while opcao != 2:
    nome = str(input('NOME: '))
    gênero = str(input('GÊNERO: '))
    idade = int(input('IDADE: '))
    dados.append([nome, gênero, idade])
    opcao = int(input('1-ADICIONAR PESSOA\n2-SAIR DO PROGRAMA'))


with open('user.csv', 'w', newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(header)
    writer.writerows(dados)

with open('user.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        print(row)
