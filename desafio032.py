choosen_year = int(input('Digite um ano: '))
if choosen_year % 4 == 0 and choosen_year % 100 != 0:
  print('O ano de {} é bisexto'.format(choosen_year))
else:
  print('O ano de {} não é bisexto'.format(choosen_year))