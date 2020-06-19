def leia_int(mensagem):
  try:
    valor = int(input('Digite um número inteiro: '))
  
  except (ValueError, TypeError):
    print('O valor digitado não é um número inteiro.')
    leia_int(mensagem)

  except KeyboardInterrupt:
    print('O usuário preferiu não digitar esse valor.')

  else:
    print(f'O número digitado foi {valor}')


def leia_float(mensagem):
  try:
    valor = float(input(mensagem))
  
  except (ValueError, TypeError):
    print('O valor digitado não é decimal.')
    leia_float(mensagem)

  except KeyboardInterrupt:
    print('O usuário preferiu não digitar esse valor.')

  else:
    print(f'O valor digitado foi {valor}')


# main

leia_int('Digite um valor inteiro: ')
leia_float('Digite um valor decimal: ')