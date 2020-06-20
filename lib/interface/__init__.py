# Sistema modular

import os
import time
from lib.arquivo import *

def run():

  if not existe('cadastro.txt'):
    criar_arquivo('cadastro.txt')

  while True:
    print_linha('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-' * 42)
    
    try:
      opcao = int(input('Sua opção: '))
    
    except (ValueError, TypeError):
      print('Erro! Digite um valor inteiro válido')
      time.sleep(2)
      os.system('cls')
   
    except KeyboardInterrupt:
      print('Erro! Digite uma opção válida')
      time.sleep(2)
      os.system('cls')

    else:

      if opcao < 1 or opcao > 3:
        print('Digite uma opção válida')
        time.sleep(2)
        os.system('cls')

      elif opcao == 1:
        listar_pessoas()
      
      elif opcao == 2:
        cadastrar_pessoa()
      
      elif opcao == 3:
        print_linha('PROGRAMA FINALIZADO')
        time.sleep(2)
        break
    


def listar_pessoas():
  print_linha('PESSOAS CADASTRADAS')


  if existe('cadastro.txt'):
    with open('cadastro.txt', 'r') as arq:
      for string in arq:
        print(string)

    arq.close()


def cadastrar_pessoa():
  print_linha('CADASTRAR PESSOAS')
  
  nome = input('Nome: ')
  idade = input('Idade: ')
 
  with open('cadastro.txt', 'a') as arquivo:
    arquivo.write(f'{nome:<30} {idade:>5} anos\n')
  
  arquivo.close()


def print_linha(mensagem):
  print('-' * 42)
  print(mensagem.center(42))
  print('-' * 42)

