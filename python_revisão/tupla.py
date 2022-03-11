num = (int(input('Digite um valor')), int(input('outro:')), int(input('Outro:')), int(input('Outro')))
par = 0
print(f'Os números foram {num}')
print(f'O número 9 aparece {num.count(9)} vez(es)')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}')
else:
    print('O número 3 não apareceu')
for c in range(0, 4):
    if num[c]/2 == num[c]//2:
        par += 1
print(f'Tem {par} números pares')
