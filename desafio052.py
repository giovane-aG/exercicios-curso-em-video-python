number = int(input('Digite um valor: '))
primo = True
for i in range(2, 10):
    if number % i == 0 and number != i:
        primo = False
if primo:
    print(number,'é um número primo')
else:
    print(number,'não é um número primo')