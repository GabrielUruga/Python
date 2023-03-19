nome = (input('Digite seu nome: '))
nome = nome.upper()
import os
os.system('cls')

peso = int(input('Digite seu peso atual: '))
import os
os.system('cls')

altura = float(input('Digite a sua altura em metros (ex: 1.75): '))
import os
os.system('cls')

imc = peso/pow(altura, 2)

print(f'{nome.capitalize()},\n\nVocê tem {altura:.2f} metros de altura e pesa {peso} kgs\n\nO seu IMC é {imc:.3f} atualmente\n\n')