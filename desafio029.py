car_speed = float(input('Velocidade atual do carro: '))
if car_speed <= 80:
  print('{} Km/H, dentro do limite')
else:
  ticket = 7 * (car_speed -80)
  print('Você está voando, passou {} Km/H do limite de 80 Km/H. Sua multa será de R$ {}'.format(car_speed - 80, ticket))