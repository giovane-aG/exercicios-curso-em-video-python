segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

# 1 dia = 24 horas
# 1 hora = 60 minutos
# 1 minuto = 60 segundos


dias = segundos / 3600 / 24
horas = dias % segundos / 24
minutos = horas % segundos / 60
segundos = minutos % segundos

print(dias, horas, minutos, segundos)
