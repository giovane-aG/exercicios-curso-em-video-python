números = []

for i in range(0, 4):
    números.append(float(input('Digite um valor: ')))

maior = max(números)
menor = min(números)

posições_maior = []
posições_menor = []

for i in range(0, len(números)):
    if números[i] == maior:
        posições_maior.append(números.index(maior, i))

    if números[i] == menor:
        posições_menor.append(números.index(menor, i))

print(f'O maior valor está na(s) posição(ões) '
      f'{posições_maior} e foi {maior}.\n'
      f'O menor valor está na posição '
      f'{posições_menor} e foi {menor}.')