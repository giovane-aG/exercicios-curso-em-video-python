entrada = input('Digite algo: ')
print('O valor digitado é do tipo {}'.format(type(entrada)))
print('É do alfabeto? {}'.format(entrada.isalpha()))
print('É um número? {}'.format(entrada.isnumeric()))
print('É alfanúmerico? {}'.format(entrada.isalnum()))
print('É um número real? {}'.format(entrada.isdecimal()))
print('É imprimível? {}'.format(entrada.isprintable()))
print('Está capitalizado? {}'.format(entrada.istitle()))