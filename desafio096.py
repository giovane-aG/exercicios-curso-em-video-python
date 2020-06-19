def calcular_área(largura, comprimento):
  area = largura * comprimento
  print(f'A área de um terreno de {largura}x{comprimento} é de {area}m².')


print('Controle de Terrenos')
print('-' * 20)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
calcular_área(largura, comprimento)