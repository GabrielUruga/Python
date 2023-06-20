'''
Bubble Sort

def -> cria uma função no Python que pode ser utilizada diversas vezes

array != lista
array -> lista de dados DO MESMO TIPO
lista -> lista de dados

O ARRAY consegue armazenar mais de valor em um única variável
'''
# Lista criada sem ordem crescente ou decrescente
lista = [4,78,45,99,32,1,5,11,78,47,52,93,63,29,88,3,41]

# definindo uma função que contará a quantia de números na lista criada
def bubble_sort(array):
    qtd = len(array)

    # Para cada elemento A na lista criada
    for a in range(qtd):

        # Para cada elemento B na lista criada
        for b in range(0, qtd-a-1):

            # Se o elemento A for maior que o elemento B
            if array[b] > array[b+1]:

                # Trocar de posição os elementos A com B ou B com A
                array[b], array[b+1] = array[b+1], array[b]

    # Retorna na lista e passa número por número nessas condições
    # até que chegue ao fim e a lista esteja em ordem crescente
    return array

print(bubble_sort(lista))
# Printa a lista ordenada em crescente, como dado na condição criada