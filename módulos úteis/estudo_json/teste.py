"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""
from pessoas import *
import json

# Converte um dicionário em JSON
# útil para salvar informações de qualquer tipo
dados = json.dumps(pessoas_dicionario, indent=4)
print(dados)

# Converte JSON em um dicionário
# útil para carregar informações de qualquer tipo
dado = json.loads(pessoas_json)
print(dado)

# Exporta dicionário para arquivo JSON
with open('pessoas.json', 'w') as f:
    json.dump(pessoas_dicionario, f, indent=4)

# Importa string de um arquivo JSON e converte em dicionário
with open('pessoas.json', 'r') as f:
    data = json.load(f)

print(data)
