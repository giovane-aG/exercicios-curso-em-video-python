nome = str(input('Digite seu nome: ')).strip()
nome = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}'.format(nome[0], nome[-1]))