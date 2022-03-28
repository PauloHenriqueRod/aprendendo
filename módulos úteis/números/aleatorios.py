import random
import string

# random.randint(a, b) - GERA UM INTEIRO DE a À b
print(random.randint(10, 20))
print('-='*30)

#random.randrange() - GERA UM NÚMERO COMO SE FOSSE A FUNÇÃO RANGE
print(random.randrange(8, 125, 6))
print('-='*30)

# random.uniform(a, b) - GERA UM NÚMERO FLUTUANTE DE a Á b
print(random.uniform(8,15))
print('-='*30)

# random.random() - GERA UM NÚMERO DE PONTO FLUTUANTE ENTRE 0 E 1
print(random.random())
print('-='*30)

# random.sample(lista, k=x) - SELECIONA ALEATORIAMENTE VALORES DE UMA LISTA, 'k' É UM VALOR OPCIONAL QUE DEFINE QUANTOS ELEMENTOS VOCÊ QUER SELECIONAR
# random.choices(lista, k=x) - A MESMA COISA QUE SAMPLE, SÓ QUE PODE REPETIR ELEMENTOS
# random.choice(lista) - SELECIONA APENAS UM ELEMENTO DA LISTA
# random,shuffle(lista) - EMBARALHA A LISTA
lista = ['Paulo', 'Pedro', 'Maria', 'Guilherme', 'Priscila', 'Rodrigo']
print(random.sample(lista, k=3))
print(random.choices(lista, k=3))
print(random.choice(lista))
random.shuffle(lista)
print(lista)


print(f'{"-"*30}GERAR SENHA ALEÁTORIA{"-"*30}')
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%$¨&*()'
geral = letras + digitos + caracteres
senha = ''.join(random.choices(geral, k=20))
print(senha)