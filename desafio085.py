valores = [[],[]]

for i in range(0, 7):
  valor = int(input(f'Digite o {i + 1}o. valor: '))
  if valor % 2 == 0:
    valores[1].append(valor)
  else:
    valores[0].append(valor)

valores[0].sort()
valores[1].sort()

print('Os valores pares digitados foram: ', end=' ')
for valor in valores[1]:
  print(valor, end=' ')

print('\nOs valores ímpares digitados foram: ', end=' ')
for valor in valores[0]:
  print(valor, end=' ' )