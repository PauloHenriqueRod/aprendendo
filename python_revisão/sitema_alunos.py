aluno = list()
lista_alunos = list()

while True:
    nome = str(input('NOME DO ALUNO: '))
    if nome == '':
        break
    nota1 = str(input('NOTA 1:')).replace(',', '.').strip()
    nota2 = str(input('NOTA 2: ')).replace(',', '.').strip()
    aluno.append(nome)
    aluno.append(float(nota1))
    aluno.append(float(nota2))
    lista_alunos.append(aluno[:])
    aluno.clear()
print('{:.<5}{:.<15}{:.>10}'.format('Nº', 'Nome', 'Média'))
for c in range(0, len(lista_alunos)):
    print(f'{c+1:<5}{lista_alunos[c][0]}{(lista_alunos[c][1]+lista_alunos[c][2])/2:>10.1f}')

with open('ALUNOS-NOTAS.txt', 'a+') as file:
    for nome in lista_alunos:
        file.write(f'{nome}\n')
        file.seek(0, 0)
