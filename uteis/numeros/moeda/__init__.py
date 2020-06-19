def metade(valor):
    return valor * 0.5


def dobro(valor):
  return valor + valor


def aumentar(valor, porcentagem):
  '''
  @params valor a ser aumentado
  @param porcentagem a ser adicioonada
  '''
  return valor + valor * porcentagem / 100


def reduzir(valor, porcentagem):
  '''
  Função que reduz do valor passado, a porcentagem escolhida
  '''
  return valor - valor * porcentagem / 100
