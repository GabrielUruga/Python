import random
n1 = input('Digite um nome: ')
n2= input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')
list = [n1, n2, n3, n4]
random.shuffle(list)
print(f'A ordem da apresentação será {list}')

# or

from random import shuffle
n1 = input('Digite um nome: ')
n2= input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')
list = [n1, n2, n3, n4]
shuffle(list)
print(f'A ordem da apresentação será {list}')

