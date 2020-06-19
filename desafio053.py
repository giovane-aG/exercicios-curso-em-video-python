phrase = input('Digite uma frase:\n').replace(' ', '').strip().lower()
middle = (len(phrase) // 2)

palíndromo = True

for i in range(0, middle):
    if phrase[i] != phrase[-(i + 1)]:
        palíndromo = False
if palíndromo:
    print('A palavra é um palíndromo')
else:
    print('A palavra não é um palíndromo')