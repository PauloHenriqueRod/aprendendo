import datetime

d = datetime.date(2001, 10, 25)
hoje = datetime.date.today()
timedelta = datetime.timedelta(hours=12)
print(hoje + timedelta)

outro_dia = datetime.date(2020, 2, 15)
diferenca_dia = outro_dia - hoje
print(diferenca_dia)

data_agora = datetime.datetime.now()
print(data_agora.strftime('%B %d, %Y'))
