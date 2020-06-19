jogador = dict()
nome = input('Nome: ')
número_partidas = int(input('Número de partidas: '))

lista = list()
n_gols = 0

for i in range(0, número_partidas):
  gols = int(input(f'Número de gols na partida {i}: '))
  n_gols += gols
  lista.append(gols)

jogador['nome'] = nome
jogador['aproveitamento'] = lista
jogador['gols'] = n_gols

print(f'O jogador {jogador["nome"]} jogou {número_partidas} partidas.')
for index, value in enumerate(lista):
  print(f'\t=> Na partida {index}, fez {value} gols.')
print(f'Foi um total de {jogador["gols"]} gols.')
