import math
cat_adjacente = float(input('Digite o tamanho do cateto adjacente: '))
cat_oposto = float(input('Digite o tamanho do cateto oposto: '))
hipotenusa = math.sqrt(cat_adjacente**2 + cat_oposto**2)
print(hipotenusa)