from datetime import date, timedelta, datetime

d = date(2001, 10, 25)
hoje = date.today()
timedelta = timedelta(hours=12)
print(hoje + timedelta)

outro_dia = date(2020, 2, 15)
diferenca_dia = outro_dia - hoje
print(diferenca_dia)

data_agora = datetime.now()
print(data_agora.strftime('%B %d, %Y'))
