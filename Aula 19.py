pessoas = {'nome': 'Josvane', 'idade': 25, 'sexo': 'M'}

print(pessoas)
print(pessoas.keys())
print(pessoas.items())
print(pessoas.values())
print('\n')

for key, value in pessoas.items():
  print(f'{key} = {value}')

del(pessoas['sexo'])
print('\n')

for key, value in pessoas.items():
  print(f'{key} = {value}')

print('\n')

brasil = list()

estado1 = {'uf':'Minas Gerais', 'sigla':'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
print(brasil[1]['sigla'])