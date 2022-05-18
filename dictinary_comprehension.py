"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:
lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:
tupla = (1, 2, 3, 4) # 1, 2, 3, 4

Se quisermos criar um set/conjunto:
conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:
dicionario = {'a': 1 , 'b': 2, 'c': 3, 'd': 4}

# Sintaxy

{chave: valor for valor in inter[avel}


 Exemplo 1:

numeros = {'a': 1 , 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor * 2 for chave, valor in numeros.items()}

print(numeros)
print(quadrado)

# Retorno / Saída:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}


# Exemplo 2: - Usando uma lista para criar um dicionário ( Lembrando que não podemos ter repetição de chave )

numero = [1, 2, 3, 4, 5, 1, 2]

quadrados = {valor: valor * 2 for valor in numero}

print(numero)
print(quadrados)

# Retorno / Saída:
# 1, 2, 3, 4, 5, 1, 2]
# {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}


# Exemplo 3: Usando uma string e uma lista para criar um dicionário

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(chaves)
print(valores)
print(mistura)

# Retorno / Saída:
# abcde
# [1, 2, 3, 4, 5]
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# Exemplo 4 - Usando logica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)

# Retorno / Saída:
# {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}
"""








































