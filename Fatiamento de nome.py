name = input ('Digite o seu nome: ')
name = name.upper()
import os
os.system ('cls')

age = input('Digite a sua idade: ')
import os
os.system('cls')

if name and age:
    print(f'O seu nome é {name.capitalize()}')

    print (f'O seu nome invertido é {name[::-1].capitalize()}')

    if ' ' in name:
        print(f'Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')

    print(f'Seu nome tem {len(name)} letras')

    print(f'A primeira letra do seu nome é {name[0]}')

    print(f'A última letra do seu nome é {name[-1]}')
else:
    print('Desculpa, você deixou campos obrigatórios em vazio')
