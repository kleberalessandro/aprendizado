"""
Módulo Collections - Counter (Contador)

https://docs.python.org/3.9/library/collections.html#collections.Counter

Collections -> High Performance Container Datetypes

Counter -> Recebe um iterável como parametro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário, contendo como chave o elemento da lista passado como parâmetro e como valor a quantidade de ocorrência
desse elemento.


# Utilizando o Counter

from collections import Counter

# Exemplo 1:

# Podemos utilizar qualque iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 45, 45, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

# Retorno:
# <class 'collections.Counter'>

print(res)

# Retorno:
# Counter({1: 5, 5: 5, 2: 4, 3: 4, 4: 4, 45: 2, 66: 1, 43: 1, 34: 1}) - Para cada elemento da lista o Counter criou uma
# chave e colocou como valor a quantidade de ocorrências.


# Exemplo 2:

# Podemos utilizar qualque iterável, aqui usamos uma string
print(Counter('Geek University'))

# Retorno:
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# OBS. Mais uma vez podemos conferir que para cada letra o Counter contou a ocorrência de cada um inclusive o espaço.


# Exemplo 3:

# Podemos utilizar qualque iterável, aqui usamos um texto:

texto = A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet sob
o princípio wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável​​, que todos possam
editar e melhorar. O projeto é definido pelos princípios fundadores. O conteúdo é disponibilizado sob a licença Creative
Commons BY-SA e pode ser copiado e reutilizado sob a mesma licença — mesmo para fins comerciais — desde que respeitando
os termos e condições de uso.

palavras = texto.split()
res = Counter(palavras)
print(res)

# Retorno:
# Counter({'e': 6, 'é': 3, 'sob': 3, 'um': 2, 'projeto': 2, 'de': 2, 'conteúdo': 2, 'que': 2, 'O': 2, 'a': 2,
# 'licença': 2, '—': 2, 'A': 1, 'Wikipédia': 1, 'enciclopédia': 1, 'colaborativa,': 1, 'universal': 1, 'multilíngue': 1,
# 'estabelecido': 1, 'na': 1, 'internet': 1, 'o': 1, 'princípio': 1, 'wiki.': 1, 'Tem': 1, 'como': 1, 'propósito': 1,
# 'fornecer': 1, 'livre,': 1, 'objetivo': 1, 'verificável\u200b\u200b,': 1, 'todos': 1, 'possam': 1, 'editar': 1,
# 'melhorar.': 1, 'definido': 1, 'pelos': 1, 'princípios': 1, 'fundadores.': 1, 'disponibilizado': 1, 'Creative': 1,
# 'Commons': 1, 'BY-SA': 1, 'pode': 1, 'ser': 1, 'copiado': 1, 'reutilizado': 1, 'mesma': 1, 'mesmo': 1, 'para': 1,
# 'fins': 1, 'comerciais': 1, 'desde': 1, 'respeitando': 1, 'os': 1, 'termos': 1, 'condições': 1, 'uso.': 1})

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

# Retorno:
# [('e', 6), ('é', 3), ('sob', 3), ('um', 2), ('projeto', 2)]
"""

















