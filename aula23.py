try:
  a = int(input('Numerador: '))
  b = int(input('Denominador: '))
  divisão = a / b

except ZeroDivisionError:
  print('Você tentou fazer um divisão por 0')

except ValueError:
  print('Você inseriu um valor que não é do tipo inteiro')

except KeyboardInterrupt:
  print('Você preferiu não inserir valores')

except Exception as erro:
  print(f'A causa do erro foi {erro.__cause__}')

else:
  print(f'{divisão:.2f}')

finally:
  print('Programa finalizado.')