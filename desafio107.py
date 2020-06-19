from uteis.numeros import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando {p} em 10% {moeda.aumentar(p, 10)}')
print(f'Reduzindo {p} em 20% {moeda.reduzir(p, 20)}')