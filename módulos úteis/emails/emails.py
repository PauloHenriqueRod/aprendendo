from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

email_enviar = str(input('EMAIL: '))
senha = str(input('SENHA: '))

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Paulo Henrique', data=data_atual)


msg = MIMEMultipart()
dequem = str(input('From: '))
paraquem = str(input('Para(email): '))
msg['from'] = dequem
msg['to'] = paraquem
msg['subject'] = 'Email de testes'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpg') as imagem:
    img = MIMEImage(imagem.read())
    msg.attach(img)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_enviar, senha)
    smtp.send_message(msg)
    print('Email enviado com sucesso')
