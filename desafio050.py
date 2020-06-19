soma = 0
for i in range(0,6):
  valor = int(input('Digite um valor: '))
  if valor % 2 == 0:
    soma += valor
print('A soma dos valores pares digitados é de', soma)