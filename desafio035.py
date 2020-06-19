print('Digite as medidas de três retas: ')
side1 = float(input('Reta 1: '))
side2 = float(input('Reta 2: '))
side3 = float(input('Reta 3: '))
if side1 > side2 + side3 or side2 > side1 + side3 or side3 > side1 + side2:
  print('Não é possível montar um triângulo com essas três retas')
else:
  print('É possível montar um triângulo com essas três retas')