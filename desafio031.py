distance = float(input('Digite a distância da viagem: '))
if distance <= 200.00:
  print('O preço da passagem será de {}'.format(distance * 0.5))
else:
  print('O preço da passagem será de {}'.format(distance * 0.45))