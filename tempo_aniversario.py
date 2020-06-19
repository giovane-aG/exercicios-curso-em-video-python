from datetime import datetime

hoje = datetime.now()
aniversário = datetime(2021, 3, 27)

tempo_espera = aniversário - hoje
print(tempo_espera)