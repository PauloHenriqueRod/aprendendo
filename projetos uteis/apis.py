# APIS: Quando o programa precisa consumir dados de terceiros, muitas vezes precisa-se acessar na internet dados para serem usados em sua aplicação. A linguagem usada para traduzir esses dados para os aplicativos é chamada de APIS.

import requests

url = 'https://api.exchangerate-api.com/v6/list'
req = requests.get(url)
print(req.status_code)
dados = req.json()


valor_reais = float(input('DIGITE UM VALOR EM R$: '))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dolar valem US${(valor_reais / cotacao):.2f}')
