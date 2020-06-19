def fatorial(num, show=False):
  fat = 1

  while (num > 0):
    if show:
      if num > 1:
        print(f'{num} x ', end='')
      else: print(f'{num} = ', end='')
    fat *= num
    num -= 1

  return fat

print(fatorial(10))
