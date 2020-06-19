print('Digite as informações de quatro pessoas: \n')

média = 0
mulheres = 0
mais_velho = ''
maior_idade = 0

for i in range(0, 2):
  nome = input('Nome: ')
  sexo = input('Sexo: ').upper()
  idade = int(input('Idade: '))
  
  média += idade

  if idade > maior_idade and sexo == 'M':
    maior_idade = idade
    mais_velho = nome

  if sexo == 'F' and idade < 20:
    mulheres += 1

print('A idade média é de {}'.format(média / 3))
print('O homem mais velho é {}'.format(mais_velho))
print('O número de mulheres com menos de 20 anos é {}'.format(mulheres))