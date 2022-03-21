with open('tarefas.txt', 'a+') as file:
    while True:
        tarea = str(input('1 - VER TAREFAS\n'
                          '2 - ADICIONAR TAREFA\n'
                          '3 - ENCERRAR PROGRAMA\n'))
        if tarea.strip() == '1':
            file.seek(0, 0)
            print(file.read())
        elif tarea.strip() == '2':
            tarefa = str(input('QUAL TAREFA DESEJA ADICIONAR?\n'))
            file.write(f'{tarefa}\n')
        elif tarea.strip() == '3':
            break
        else:
            print('\033[32mDIGITE UMA OPÇÃO VÁLIDA\033[m')
