persons = list()
_continue = 'S'

while _continue.upper() == 'S':
  name = input('Name: ')
  weight = float(input('Peso: '))
  person = [name, weight]
  persons.append(person)
  _continue = input('Deseja continuar?[S/N]: ')

quantity = len(persons)

heavier = 0
lighter = 1000
for person in persons:
  if person[1] > heavier:
    heavier = person[1]
  elif person[1] < lighter:
    lighter = person[1]

heaviest_persons = []
lightest_persons = []

for person in persons:
  if person[1] == heavier:
    heaviest_persons.append(person[0])
  elif person[1] == lighter:
    lightest_persons.append(person[0])

print(f'Ao todo você cadastrou {quantity} pessoas.')
print(f'O maior peso foi de {heavier}Kg. Peso de ', end='')
for person in heaviest_persons:
  print(person, end=' ')
print('.')

print(f'O menor peso foi de {lighter}Kg. Peso de ', end='')
for person in lightest_persons:
  print(person, end=' ')
print('.')