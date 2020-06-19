from random import randint
from time import sleep
from operator import itemgetter

resultados = dict()

for i, value in enumerate(range(0, 4)):
  resultados[f'jogador{i}'] = randint(1, 6)

ranking = dict()

print('Valores sorteados:')
for k, v in resultados.items():
  print(f'O {k} tirou {v} no dado.')
  sleep(1)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
  print(f'{i + 1}ª lugar foi o jogador {v[1]}')
