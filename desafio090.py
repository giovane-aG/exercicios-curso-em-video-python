pessoa = dict()
nome = str(input('Nome: '))
média = float(input(f'Média de {nome}: '))

pessoa['nome'] = nome
pessoa['média'] = média
if pessoa['média'] >= 6:
  pessoa['situação'] = 'Aprovado'
else:
  pessoa['situação'] = 'Reprovado'
print(f'A média de {pessoa["nome"]} é {pessoa["média"]}, então está {pessoa["situação"]}.')