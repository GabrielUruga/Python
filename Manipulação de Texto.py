frase = 'Curso em Vídeo Python'
# uma frase vai para a memória separada em caracteres, onde o ponto inicial é 0

# Fatiamento
frase[9]
print(frase[9])

frase[9:13]
print(frase[9:13])
frase[9:21]
print(frase[9:21])
# O último número não é considerado

frase[9:21]
print(frase[9:21:2])
#  caracteres de 9 até 20 saltando de 2 em 2

frase[:5]
print(frase[:5])
# Mesmo que [0:5], em que é printado do 0 ao 15

frase[15:]
print(frase[15:])
# Fatia do valor indicado até o final da frase

frase[9::3]
print(frase[9::3])
# Vai do 9 ao final saltando de 3 em 3


#  Análise

# comando LEN
print(len(frase))
# conta o total de caracteres da frase

# comando COUNT
print(frase.count('o'))
# conta quantas vezes algo se repete dentro da frase

print(frase.count('o', 0, 13))
# conta a quantia de vezes que se repete algo, porém dentro de um fatiamento determinado

# comando FIND
print(frase.find('deo'))
# apresenta em qual posição a parte 'deo' é iniciada na frase

print(frase.find('Android'))
# printa -1 pois a string não foi encontrada dentro da frase

print('Curso' in frase)
# Se a string existe  na frase, o programa diz que é verdadeiro

# Transformação

# Comando REPLACE
print(frase.replace('Python', 'Android'))
# Faz a troca das strings

# Método UPPER
print(frase.upper())
# deixa todos os caracteres da string em maiúsculo

# Método LOWER
print(frase.lower())
# deixa todos os caracteres da string em minúsculo

# Método CAPITALIZE
print(frase.capitalize())
# deixa apenas o primeiro caractere em maiúsculo

# Método TITLE
print(frase.title())
# capitaliza todos os primeiros caracteres de cada palavra

# Método STRIP
frase1 = '   Aprenda Python   '
print(frase1.strip())
# este método exclui o excesso de espaço no começo e fim

# variação R no método STRIP
frase1 = '   Aprenda Python   '
print(frase1.rstrip())
# remove apenas os espaços da direita/right

# variação L no método STRIP
frase1 = '   Aprenda Python   '
print(frase1.lstrip())
# remove apenas os espaços da esquerda/left

# Divisão
print(frase.split())
# separa em uma lista todas as strings da variável

# Junção
print('-'.join(frase))
#  realiza a junção dos caracteres com um símbolo atribuído em uma string

# printar texto longo = 3 aspas duplas no começo e no fim
print("""Na musculação existem diferentes processos que varia de acordo com o objetivo esperado pela pessoa que praticará o esporte. 
Há objetivos como: ganho de massa muscular, redução do percentual de gordura ou manter o físico atual.""")

