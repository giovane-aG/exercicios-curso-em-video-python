valores = []

i = 0
while True:
    i = int(input('Digite um valor(-1 para terminar): '))

    if i == -1: break

    if i in valores:
        print('Esse valor já foi adicionado, insira outro.')
    else:
        valores.append(i)
        print('Valor inserido')

valores.sort()
print(valores)