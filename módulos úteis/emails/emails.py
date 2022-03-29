from string import Template
from datetime import datetime

with open('testando_emails.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Luiz Otávio', data=data_atual)

print(corpo_msg)
