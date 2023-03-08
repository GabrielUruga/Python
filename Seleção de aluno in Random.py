import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
list = [a1, a2, a3, a4]
# Lista qualquer, em que insiro todas as possibilidades que quero
select = random.choice(list)
# random.choice é um módulo de escolha aleatória dentro de uma lista
print(f'O aluno escolhido foi: {select}')

# or

from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
list = [a1, a2, a3, a4]
select = choice(list)
print(f'O aluno escolhido foi {select}')