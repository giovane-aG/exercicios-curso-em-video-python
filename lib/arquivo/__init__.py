def existe(nome):
  try:
    arquivo = open(nome, 'rt')
    arquivo.close()
  except FileNotFoundError:
    return False
  else:
    return True


def criar_arquivo(nome):
  try:
    arquivo = open(nome, 'wt+')
    arquivo.close()
  except:
    print('Erro ao criar o arquivo')