# file = open('abc.txt', 'w+')
# file.write('FLU\n')
# file.write('linha\n')
# file.write('tantantan\n')
#
# file.seek(0, 0)
# print('LENDO LINHAS: ')
# print(file.read())
# print('-'*30)
#
# file.seek(0, 0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# file.close()

with open('abc.txt', 'a+') as file:
    file.write('FLU\n')
    file.seek(0, 0)
    print(file.read())
