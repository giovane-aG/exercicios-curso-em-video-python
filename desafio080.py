valores = []

for i in range(0, 5):
    valor = int(input('Digite um valor: '))

    if len(valores) == 0:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        # [10, 11]
        while pos < len(valores):
            if valor > valores[pos]:
                pos += 1
            else: break

        if pos == len(valores):
            valores.append(valor)
            print(f'Adicionado ao final da lista...')
        else:
            valores.insert(pos, valor)
            print(f'Adicionado na posição {pos} da lista...')

print('Os valores em ordem são', end=' ')
for valor in valores:
    print(valor, end=' ')
