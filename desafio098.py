from time import sleep


def contar(ini, fim, passo):
  """
  -> Função criada para realizar uma contagem
  :param ini: Início da contagem
  :param fim: Fim da contagem
  :param passo: Progressão da contagem
  :return: sem retorno
  Função criada por Giovane Aguiar de Almeida
  """
  print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
  sleep(2.5)

  if ini > fim:
    passo *= -1
    fim -= 1
  for i in range(ini, fim, passo):
    print(i, end=' ', flush=True)
    sleep(.3)

  print('FIM!')


def sua_vez():
  print('Agora é sua vez de personalizar a contagem!')
  ini = int(input('Início: '))
  fim = int(input('Fim: '))
  passo = int(input('Passo: '))

  if ini > fim:
    passo *= -1
    fim -= 1
  else:
    fim += 1
  for i in range(ini, fim, passo):
    print(i, end=' ', flush=True)
    sleep(.3)


contar(1, 10, 1)
contar(10, 0, 2)
sua_vez()
