produtos = ('Lápis', 1.75, 
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 6.00, 
            'Transferidor', 10.00,
            'Calculadora', 20.00, 
            'Mochila', 32.00)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for i in range(0, len(produtos)):
  if i % 2 == 0:
    print(f'{produtos[i]:.<30}', end = '')
  else:
    print(f'R$ {produtos[i]:>7.2f}')
print('-' * 40)