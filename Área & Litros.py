# Método I

alt = int(input('Qual a altura dessa parede? '))
comp = int(input('Qual o comprimento dessa parede? '))

area = alt*comp
ltintas = area/2

print ('A área da parede vale {} metros e a quantia de tinta necessária é de {} litros.'.format(area,ltintas))

# Método II

alt = float(input('Qual a altura dessa parede? '))
comp = float(input('Qual o comprimento dessa parede? '))

print (f'A área da parede vale {alt*comp} metros e a quantia de tinta necessária é de {(alt*comp)/2} litros.')