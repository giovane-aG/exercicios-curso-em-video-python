numbers = []
pares = []
ímpares = []

_continue = True

while _continue:
    number = int(input('Digite um número: '))
    numbers.append(number)
    if number % 2 == 0:
        pares.append(number)
    else:
        ímpares.append(number)
    if input('Deseja continuar?[S/N]: ').upper() == 'N':
        _continue = False

print('Valores digitados: ', end=' ')
for number in numbers:
    print(number, end=' ')

print('\nValores pares: ', end=' ')
for par in pares:
    print(par, end=' ')

print('\n Valores ímpares: ', end=' ')
for ímpar in ímpares:
    print(ímpar, end=' ')