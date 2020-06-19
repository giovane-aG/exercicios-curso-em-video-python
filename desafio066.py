n = 0
soma = 0
count = 0

while True:
  n = int(input('Digite um valor(ou 999 para terminar): '))
  if n == 999:
    break
  soma += n
  count += 1

print(f'A soma dos {count} valor(res) digitado(s) é {soma}')