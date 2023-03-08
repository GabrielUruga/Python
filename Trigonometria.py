from math import sqrt
co = float(input('Valor do cateto oposto:'))
ca = float(input('Valor do cateto adjacente:'))
h = co**2 + ca**2
hf = sqrt(h)
print(f'O valor da hipotenusa é {hf:.2f}')

#or

from math import hypot
co = float(input('Valor do cateto oposto:'))
ca = float(input('Valor do cateto adjacente:'))
h = hypot(co,ca)
print(f'O valor da hipotenusa é {h:.2f}')