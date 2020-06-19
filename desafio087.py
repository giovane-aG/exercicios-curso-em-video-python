matrix = []
even_sum = 0
third_column_sum = 0
second_line_biggest_value = 0

for i in range(3):
  matrix.append([0] * 3)

for i in range(3):
  for j in range(3):
    value = int(input(f'Digite o valor da posição [{i}][{j}]: '))
    matrix[i][j] = value

    if value % 2 == 0: even_sum += value
    if j == 2: third_column_sum += value

second_line_biggest_value = max(matrix[1])

for i in range(3):
  print(matrix[i])

print(f'A soma dos valores pares foi {even_sum}')
print(f'A soma dos valores da terceira coluna é {third_column_sum}')
print(f'O maior valor da segundo linha é {second_line_biggest_value}')