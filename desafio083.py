expression = input('Digite uma expressão: ')

open_parentheses = 0
closed_parentheses = 0

valid_expression = True
achou = False

boolean_list = []

for i in range(0, len(expression)):
  boolean_list.append(False)

for index, char in enumerate(expression):
  if char == '(':
    open_parentheses += 1
    pos = index
    achou = False

    while pos < len(expression) or not achou:

      if expression[pos] == ')' and boolean_list[pos] == False:
        boolean_list[pos] = True
        closed_parentheses += 1
        achou = True

      pos += 1

    if pos == len(expression) and not achou:
      valid_expression = False
      break

  elif expression[index] == ')' and boolean_list[index] == False:
    closed_parentheses += 1

if open_parentheses == closed_parentheses and valid_expression:
  print('Expressão válida')
else:
  print('Expressão inválida')
