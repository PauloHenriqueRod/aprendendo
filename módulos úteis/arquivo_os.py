import os

def formata_tamanho(tamanhos):
    base = 1024
    kilo = base
    mega = base**2
    giga = base**3
    tera = base**4
    peta = base**5
    if tamanhos < base:
        texto = 'B'
    elif tamanhos < mega:
        tamanhos /= kilo
        texto = 'K'
    elif tamanhos < giga:
        tamanhos /= mega
        texto = 'M'
    elif tamanhos < tera:
        tamanhos /= giga
        texto = 'G'
    elif tamanhos < peta:
        tamanhos /= tera
        texto = 'T'
    else:
        tamanhos /= peta
        texto = 'P'
    return f'{round(tamanhos, 2)}{texto}'

caminho_procura = input('Caminho do arquivo: ').replace('\\', '/')
termo_procura = input('Termo para procurar: ').lower()
conta = 0  

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        try:
            if termo_procura in arquivo:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print()
                print(f'Encontrei o arquivo {arquivo}')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {ext_arquivo}')
                print(f'Tamanho {tamanho}')
                print(f'Tamanho formatado {formata_tamanho(tamanho)}')
        except PermissionError as r:
            print('SEM PERMISSÕES')
        except SyntaxError as r:
            print('ERRO DE SÍNTAXE')
        except FileNotFoundError as r:
            print('ARQUIVO NÃO ENCONTRADO')
        except Exception as r:
            print('ERRO DESCONHECIDO ENCONTRADO')

print()
print(f'{conta} ARQUIVOS ENCONTRADO(S)')