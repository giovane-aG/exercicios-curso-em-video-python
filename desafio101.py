from datetime import date

def voto():
  data = date.today().year
  ano = int(input('Em que ano você nasceu? '))
  idade = data - ano
  if idade < 16:
    return f'Com {idade}: NÃO VOTA.'
  elif idade >= 16 and idade < 18:
    return f'Entre 16 e 18 anos: VOTO OPCIONAL.'
  elif idade > 65:
    return f'Com {idade} anos: VOTO OPCIONAL.'
  elif idade >= 18:
    return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print(voto())