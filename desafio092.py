from datetime import date

nome = ''
ano_nascimento = 0
carteira_trabalho = 0
continuar = 'S'

nome = input('Nome: ').strip()
ano_nascimento = int(input('Ano de nascimento: '))
carteira_trabalho = int(input('Número da carteira de trabalho: '))

pessoa = dict()
pessoa['nome'] = nome
ano_atual = date.today().year
pessoa['idade'] = ano_atual - ano_nascimento
pessoa['ctps'] = carteira_trabalho

if carteira_trabalho != 0:
  ano_contrato = int(input('Ano de contratação: '))
  pessoa['contratação'] = ano_contrato
  salário = float(input('Salário: '))
  pessoa['salário'] = salário
  aposentadoria = pessoa['idade'] + 35
  pessoa['aposentadoria'] = aposentadoria

for key, value in pessoa.items():
  print(f'{key}: {value}')
