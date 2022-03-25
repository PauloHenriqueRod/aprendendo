import os
import shutil

caminho_antigo = input('CAMINHO ANTIGO: ').replace('\\', '/')
caminho_novo = input('CAMINHO NOVO: ').replace('\\', '/')

try:
    os.mkdir(caminho_novo)
except FileExistsError:
    print(F'PASTA {caminho_novo} JÁ EXISTE')

for raiz, diretorios, arquivos in os.walk(caminho_antigo):
    for arquivo in arquivos:
        local_antigo = os.path.join(raiz, arquivo)
        local_novo = os.path.join(caminho_novo, arquivo)
        print(local_novo)
        try:
            shutil.move(local_antigo, local_novo)
            print(f'{arquivo} movido para {caminho_novo}')
        except Exception:
            pass
