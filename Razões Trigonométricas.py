import math
a = float(input('Digite o ângulo desejado: '))
s = math.sin(math.radians(a))
print(f'O Ângulo {a} tem o Seno de {s:.2f}')
c = math.cos(math.radians(a))
print(f'O Ângulo {a} tem o Cosseno de {c:.2f}')
t = math.tan(math.radians(a))
print(f'O Ângulo {a} tem a Tangente de {t:.2f}')

#or

from math import radians,sin,cos,tan
a = float(input('Digite o ângulo desejado: '))
s = sin(radians(a))
print(f'O Ângulo {a} tem o Seno de {s:.2f}')
c = cos(radians(a))
print(f'O Ângulo {a} tem o Cosseno de {c:.2f}')
t = tan(radians(a))
print(f'O Ângulo {a} tem a Tangente de {t:.2f}')
