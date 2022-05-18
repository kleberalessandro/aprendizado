"""
Módulo Collections - Deque
https://docs.python.org/3.9/library/collections.html#collections.deque

Podemos dizer que o deque é uma lista de alta performace.


# Fazendo import

from collections import deque

# Criando deques

deq = deque('Geek')
print(deq)

# Retorno
# (['G', 'e', 'e', 'k'])

# Adicionando elementos no deque
deq.append('y') # Adiciona no final
print(deq)

# Retorno:
# (['G', 'e', 'e', 'k', 'y'])

# Utilizando o appendlft - Adiciona no começo ou seja com deque podemos adicionar tanto no final como no início da lista

deq.appendleft('k')
print(deq)

# Retorno
# (['k', 'G', 'e', 'e', 'k', 'y'])

# Removendo elemento

print(deq.pop()) # Remove e retorno o último elemento
print(deq)

# Retorno:
# y
# deque(['k', 'G', 'e', 'e', 'k'])

print(deq.popleft()) # Remove e retorno o primeiro elemento
print(deq)

# Retorno:
# k
# deque(['G', 'e', 'e', 'k'])

"""

