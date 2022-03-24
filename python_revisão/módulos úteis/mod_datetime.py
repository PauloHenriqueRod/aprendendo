from datetime import datetime, timedelta

nasc = datetime(2001, 10, 25, 10, 25, 23)
# CRIAR UMA DATA
print(nasc)

print(nasc.strftime('%d/%m/%Y %H:%M:%S'))
# data.strftime(format) = ALTERA O FORMATO DE UMA DATA

print(datetime.strptime('20/4/2019', '%d/%m/%Y'))
# datime.strptime(str, format) = TRANSFORMA UMA STRING EM UMA DATA

print(nasc.timestamp())
# data.timestamp() = CALCULA A QUANTIDADE DE SEGUNDOS DESDE 1970

print(datetime.fromtimestamp(1004016323.0))
# datime.timestamp(float) = ENCONTRA UMA DATA À PARTIR DO TIMESTAMP

data = datetime.strptime('20/04/2005 20:00:00', '%d/%m/%Y %H:%M:%S')
dif = data - nasc
print(dif.seconds)