# Fatiamento de Strings(cadeias de caracteres)
frase = 'Curso em vídeo python'
print(frase[:5])
print(frase[1:4])
print(frase[5:19:2])
print(frase[9::3])

# Análise de Strings
# Tamanho da String
print(len(frase))

# Contar quantas vezes determinado caracter aparece
print(frase.count('o'))

# Selecionar as ocorrências de uma string dentro de outra String
# em um intervalo determinado
print(frase.count('o',0, 13))

# Retorna o índice do primeiro caracter da string, caso esteja na String
print(frase.find('deo'))

# Retorna True caso a string buscada esteja dentro da String
print('Curso' in frase)

print('Android' in frase)

# Transformação de Strings

# Substituir uma string por outra
frase1 = frase.replace('python','android')
print(frase1)

# Botar em maiúsculo
frase2 = frase.upper()
print(frase2)

# Primeira letra da String capitalizada
frase2 = frase.capitalize()
print(frase2)

# Todas as palavras da String ficam capitalizadas
frase2 = frase.title()
print(frase2)

# Remover espaços inúteis (não remove os espaços entre as palavras)
frase.strip()
# Remover os espaços da direita
frase.rstrip()
# Remover os espaços da esquerda
frase.lstrip()

# Divisão

# Divide a String (por padrão nos espaços, mas pode ser configurado)
frase2 = frase.split()
print(frase2)

# Junção
print('-'.join(frase))

# Printando um texto enorme
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum.""")