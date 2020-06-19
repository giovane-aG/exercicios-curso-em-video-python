def leia_int(mensagem):
  try:
    n = int(input(mensagem))
    return n
  except:
    print('Erro! Digite um número inteiro válido.')
    leia_int(mensagem)


n = leia_int('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')