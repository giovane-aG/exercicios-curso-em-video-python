from random import randint
number = randint(0, 5)
print('Acabei de pensar em um número entre 0 e 5. Você consegue advinhar qual?')
response = int(input('O número é: '))
if response == number:
  print('Você acertou, eu pensei no número {}'.format(number))
else:
  print('Eroou, eu pensei no número {}'.format(number))