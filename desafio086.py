matrix = []

for i in range(3):
  matrix.append([0] * 3)

for i in range(3):
  for j in range(3):
    value = int(input(f'Digite o valor da posição [{i}][{j}]: '))
    matrix[i][j] = value

for i in range(3):
  print(matrix[i])
