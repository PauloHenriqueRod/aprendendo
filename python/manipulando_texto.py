frase = '    ESTOU REVISANDO, ESTE É UM TREINO DE MANIPULAÇÃO DE TEXTO     '

# [INICIA:TERMINA:PULA DE X EM X]
print(frase[0:23:5])

# len = contagem de numéro de letras (funciona também com elementos de lista)
print(len(frase))

# frase.upper().count('A', x) conta o número de letras 'as' do texto, começa a contar a partir da posição 'x'
print(f'O seu nome possui {frase.upper().count("A")} letras as')

# frase.find('palavra') encontra onde começa a palavra no texto
print(frase.find('REVISANDO'))

# 'Paulo' in frase = TRUE -> TEM A PALAVRA NO TEXTO, FALSE -> NÃO TEM
print('PAULO' in frase)

# frase.replace('X','Y') SUBSTITUI AS PALAVRAS NO TEXTO
print(frase.replace('REVISANDO', 'ESTUDANDO'))

# lower = frase em letras minúsculas, upper = frase em letras maiúsculas
# capitalize = primeira letra em maiúculo, title = Primeira letra de cada palavra em maiúsculo
print(frase.lower())
print(frase.upper())
print(frase.capitalize())
print(frase.title())

# função strip -> retira espaços das laterais do texto, add 'r' ou 'l' para tirar apenas de um lado
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

# função split transforma uma string em uma lista
a = frase.split()

# 'x'.join(y) adiciona 'x' entre os elementos da lista 'y'
print('-'.join(a))
