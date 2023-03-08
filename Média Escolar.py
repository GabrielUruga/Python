# Método I

n1 = float(input('Digite a nota da avaliação 1:'))

n2 = float(input('Digite a nota da avaliação 2:'))

media = (n1+n2)/2


print ('A média do aluno é: {}'.format(media))

# Método II

n1 = float(input('Digite a nota da avaliação 1: '))
n2 = float(input('Digite a nota da avaliação 2: '))

print (f'A média do aluno é: {(n1+n2)/2}')

# Método III

n1 = float(input('Digite a nota da avaliação 1: '))
n2 = float(input('Digite a nota da avaliação 2: '))

print (f'A média do aluno é: {(n1+n2)/2:.1f}')
# :.1f -> a nota é mostrada com apenas uma casa decimal