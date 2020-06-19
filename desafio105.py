def notas(* n, situação=False):
  lista = list()
  lista.append(n)

  resposta = dict()
  resposta['total'] = len(lista)
  resposta['maior'] = max(lista)
  resposta['menor'] = min(lista)
  resposta['média'] = sum(lista) / resposta['total']

  if situação == True:
    média = resposta['média']
    if média <= 6:
     resposta['média'] = 'Ruim'
    elif média <= 7:
      resposta['média'] = 'Razoável'
    elif média > 7:
      resposta['média'] = 'Boa'

  return resposta

resp = notas(5, 6, 7, situação=True)
print(resp)