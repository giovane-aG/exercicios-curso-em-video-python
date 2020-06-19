from random import random

n1 = int(random() * 10)
n2 = int(random() * 10)
n3 = int(random() * 10)
n4 = int(random() * 10)
n5 = int(random() * 10)

tupla = (n1, n2, n3, n4, n5)
print(tupla)

print('Menor valor gerado:',min(tupla))
print('Maior valor gerado:',max(tupla))