from urllib import request

try:
  page = request.urlopen('http://www.pudim.com.br')
except:
  print('O site pudim não está disponível')
else:
  print('o site pudim está disponível.')