frase = '    ESTOU REVISANDO, ESTE É UM TREINO DE MANIPULAÇÃO DE TEXTO     '

# [INICIA:TERMINA:PULA DE X EM X]
print(frase[0:23:5])
print('-='*30)

# len = contagem de numéro de letras (funciona também com elementos de lista)
print(len(frase))
print('-='*30)

# frase.upper().count('A', x) conta o número de letras 'as' do texto, começa a contar a partir da posição 'x'
print(f'O seu nome possui {frase.upper().count("A")} letras as')
print('-='*30)

# frase.find('palavra') encontra onde começa a palavra no texto
print(frase.find('REVISANDO'))
print('-='*30)

# 'Paulo' in frase = TRUE -> TEM A PALAVRA NO TEXTO, FALSE -> NÃO TEM
print('PAULO' in frase)
print('-='*30)

# frase.replace('X','Y') SUBSTITUI AS PALAVRAS NO TEXTO
print(frase.replace('REVISANDO', 'ESTUDANDO'))
print('-='*30)

# lower = frase em letras minúsculas, upper = frase em letras maiúsculas
# capitalize = primeira letra em maiúculo, title = Primeira letra de cada palavra em maiúsculo
# frase.replace('x', 'y') substitui a string 'x' por 'y' na frase
print(frase.lower())
print(frase.upper())
print(frase.capitalize())
print(frase.title())
print(frase.replace('A', '@'))
print('-='*30)

# função strip -> retira espaços das laterais do texto, add 'r' ou 'l' para tirar apenas de um lado
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print('-='*30)

# função split transforma uma string em uma lista
# VOCÊ PODE ESCOLHER ONDE VAI TER A QUEBRA ESCOLHENDO UM CARACTERE, À PARTIR DE UMA VIRGULA, HÍFEN, TRAVESSÃO...
a = frase.split()

# 'x'.join(y) adiciona 'x' entre os elementos da lista 'y'
print('-'.join(a))
print('-='*30)

# .isalpha = saber se é alfabético
# .isspace = se tem espaçoes
# .isupper = se tá em maiúsculas
# .islower = se tá em minúsculas

# CONVERTER FRASE PRA LISTA
frase = 'Sou tricolor de coração'
lista = list(frase)
print(lista)
print('-='*30)

# \ PODE SER USADO PARA MUDAR O SIGNIFICADO DE ALGUM CARCTERE
#  -------------------------EXEMPLOS-----------------------------------
# QUEBRAS DE LINHA = '\n'
print('Sou \nTricolor')
# INSERIR TABULAÇÃO(MARGEM) = '\t'
print('Sou \n\tTricolor')
# PARA ESCREVER \ USA-SE DUAS BARAS, \\
print('Olha a contra-barra: \\')
# PODE-SE USAR PARA "ASPAS" TAMBÉM
print('Newton disse: \"Se conseguir chegar tão longe foi porque subi no ombro de gigantes\"')
