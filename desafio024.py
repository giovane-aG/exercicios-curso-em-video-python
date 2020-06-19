cidade = input('Digite o nome de uma cidade: ')
cidade = cidade.split()
if cidade[0] == 'Santo':
    print('O nome da cidade começa com a palavra "Santo"')
elif cidade.isEmpty():
    print('Nome inválido')
else:
    print('O nome da cidade não começa com a palavra "Santo"')