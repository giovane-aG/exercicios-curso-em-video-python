_continue = 'S'
lista_sujeitos = list()
mujeres = list()
acima_média = list()
sujeito = dict()
média = 0

while _continue == 'S':
  sujeito['nome'] = input('Nome: ')
  sujeito['sexo'] = input('Sexo: ').upper()
  sujeito['idade'] = int(input('Idade: '))
  média += sujeito['idade']
  lista_sujeitos.append(sujeito.copy())

  if sujeito['sexo'] == 'F':
    mujeres.append(sujeito.copy())

  _continue = input('Deseja continuar?[s/n]:').upper()

média /= len(lista_sujeitos)

for pessoa in lista_sujeitos:
  if pessoa['idade'] > média:
    acima_média.append(pessoa.copy())

print(f'No total foram cadastradas {len(lista_sujeitos)} pessoas.\n'
      f'A idade média das pessoas cadastradas é {média} anos.\n')

print('Todas as mulheres cadastradas: ')
for mujer in mujeres:
  print(mujer['nome'], end = ' ')

print('\nPessoas acima da média do grupo: ')
for pessoa in acima_média:
  print(pessoa['nome'], end = ' ')