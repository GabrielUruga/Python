name = input ('Qual seu nome? ')
name = name.lower()
import os
os.system('cls')

idade = int(input('Qual a sua idade? '))
import os
os.system('cls')

maior = idade >= 18
if(maior == True):
    print(f'{name.capitalize()},\nVocê é de maior, avance!!\n')
else:
    print(f'Ops, {name.capitalize()}\n\nVocê não é de maior,\nAinda faltam {18-idade} ano(s)!!\n')
