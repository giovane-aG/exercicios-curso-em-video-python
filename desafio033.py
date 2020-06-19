print('Digite 3 números')
n1 = float(input('Primeiro número:'))
n2 = float(input('Segundo número:'))
n3 = float(input('Terceiro número:'))
numbers = [n1,n2,n3]
bigest = max(numbers)
smallest = min(numbers)
print('O maior número é {} e o menor é {}'.format(bigest, smallest))