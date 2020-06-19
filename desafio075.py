print('Insira quatro valores: ')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
n4 = int(input('Quarto valor: '))

tupla = (n1, n2, n3, n4)
tupla_de_pares = ()

contador = 0
noves = tupla.count(9)
print('O número 9 apareceu',noves,'vezes')

if 3 in tupla:
  print(f'O número 3 apareceu na posição {tupla.index(3)}')
else:
  print('O número 3 não está na coleção')

print('Os valores pares são ', end='')
for número in tupla:
  if número % 2 == 0:
    print(número, end=' ')

