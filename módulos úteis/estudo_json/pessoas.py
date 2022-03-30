"""
https://exchangeratesapi.io/
https://api.exchangeratesapi.io/latest
"""

pessoas_dicionario = {
    1: {
        'nome': 'Paulo Henrique',
        'sobrenome': 'Rodrigues',
        'idade': 20,
        'altura': 1.78,
        'peso': 70,
    },
    2: {
        'nome': 'Maria',
        'sobrenome': 'Oliveira',
        'idade': 52,
        'altura': 1.67,
        'peso': 57,
    },
    3: {
        'nome': 'Pedro',
        'sobrenome': 'Fará',
        'idade': 32,
        'altura': 1.95,
        'peso': 113,
    },
}

pessoas_json = """
{
    "1": {
        "nome": "Luiz Ot\u00e1vio",
        "sobrenome": "Miranda",
        "idade": 25,
        "altura": 1.8,
        "peso": 80.53
    },
    "2": {
        "nome": "Maria",
        "sobrenome": "Oliveira",
        "idade": 52,
        "altura": 1.67,
        "peso": 57
    },
    "3": {
        "nome": "Pedro",
        "sobrenome": "Faria",
        "idade": 32,
        "altura": 1.95,
        "peso": 113
    }
}
"""