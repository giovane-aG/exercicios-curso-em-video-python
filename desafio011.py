alt = int(input('Qual a altura da parede? '))
lar = int(input('Qual a largura da parede? '))
area = alt * lar
quant_tinta = area / 2
print('A area da parede é {} e a quantidade de tinta necessária para pintá-la será de {} litro(s).'.format(area, quant_tinta))
