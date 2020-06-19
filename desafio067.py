while True:
  n = int(input('De qual número você quer ver a tabuada?(Digite -1 para sair): '))
  if n == -1:
    break
  for i in range(1, 10):
    print(f'{n} x {i} = {n*i}')