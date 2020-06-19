valores_celulares = [1500, 2230, 3000, 5000]

'''

  'r' -> Usado somente para ler algo
  'w' -> Usado somente para  escrever algo
  'r+' -> Usado para ler e escrever algo
  'a' -> Usado para acresentar algo

'''

with open('valores_celulares.txt', 'a') as arquivo:
  for valor in valores_celulares:
    arquivo.write(str(f'{valor}\n'))
