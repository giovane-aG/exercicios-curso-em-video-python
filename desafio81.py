numbers = []
_continue = True

while _continue:
    numbers.append(int(input('Digite um valor: ')))
    if input('Deseja continuar?[S/N]: ').upper() == 'N':
        _continue = False

print(f'Você digitou {len(numbers)} valores.')

numbers.sort(reverse = True)

for number in numbers:
    print(number, end = ' ')

if 5 in numbers:
    print(f'\nO valor 5 foi encontrado na posição {numbers.index(5)}')
else:
    print('O valor 5 não foi encontrado')