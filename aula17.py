valores = []
valores.append(5)
valores.append(9)
valores.append(-1)

# se atribuirmos uma lista a outra e.g(lista_B = lista_A) estaremos criando
# uma ligação entre as duas listas e não uma cópia de A em B.
# Para criarmos uma cópia devemos atribuir todos os valores de A a B
# e.g(lista_B = lista_A[:])

for c, v in enumerate(valores):
    print(f'Valor {v} na posição {c}')
print('Cheguei ao final')