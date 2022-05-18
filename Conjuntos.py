"""
Conjuntos:

 - Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria dos Conjuntos da Matemática.

 - Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

 - Sets (conjuntos) não possuem valores duplicados;
 - Sets (cinjuntos) não possuem valores ordenados;
 - Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles.
Conjuntos são bons quando não precisamos se preocupar com chave, valores e itens duplicados.

Os conjuntos (Sets) são referenciados em Python com chave {}

Diferença entre conjuntos (Sets) e Mapas (Dicionários) em Python:
        - Um dicionário tem chave/valor;
        - Im conjunto tem apenas valor;


# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.
print(s)
print(type(s))

# Retorno:
# {1, 2, 3, 4, 5, 6, 7}
# <class 'set'>

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e não
# fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Retorno:
# {1, 2, 3, 4, 5}
# <class 'set'>

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Retorno:
# Tem o 3


# Importante lembrar que além de não termos valores duplicados, não temos ordem


# Listas aceita valores duplicados então teremos 10 elementos:
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista:{lista} com {len(lista)} elementos')

# Tuplas aceita valores duplicados então teremos 10 elementos:
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'tupla:{tupla} com {len(tupla)} elementos')

# Dicionários não aceita chaves duplicadas então teremos 8 elementos:
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'dicionário:{dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceita valores duplicados então teremos 8 elementos e executa uma ordenação própria do conjunto:
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'conjunto:{conjunto} com {len(conjunto)} elementos')

# Retorno:
# lista:[99, 2, 34, 23, 2, 12, 1, 44, 5, 34] com 10 elementos
# tupla:(99, 2, 34, 23, 2, 12, 1, 44, 5, 34) com 10 elementos
# dicionário:{99: 'dict', 2: 'dict', 34: 'dict', 23: 'dict', 12: 'dict', 1: 'dict', 44: 'dict', 5: 'dict'} com 8 elementos
# conjunto:{1, 2, 99, 34, 5, 12, 44, 23} com 8 elementos

# Assim com todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34, 22, 44}
print(s)
print(type(s))

# Retorno:
# {1, 34, 44, 22, 'b'}
# <class 'set'>

# Podemos iterar em um Set normalmente

for valor in s:
    print(valor,end=' ')

# Retorno
# 1 34 44 b 22

# Uso interessante em Sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou meseu e os visitantes
# Informam manualmente a cidade de onde vieram.
# Nos adicionamos cada cidade em uma lista Python, já que uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Cuiba', 'Campo Grande', 'São Paulo', 'Cuiba']

print(cidades)
print(len(cidades))

# Retorno:
# ['Belo Horizonte', 'São Paulo', 'Cuiba', 'Campo Grande', 'São Paulo', 'Cuiba']
# 6

# Agora precisamos saber quantas cidades distintas, ou seja única, temos.
# O que você faria? Faria um loop na lista..?
# Podemos utilizar o set para isso.

print(cidades)
print(len(cidades))

# Retorno:
# ['Belo Horizonte', 'São Paulo', 'Cuiba', 'Campo Grande', 'São Paulo', 'Cuiba']
# 6

print(set(cidades))
print(len(set(cidades)))

# Retorno:
# {'São Paulo', 'Cuiba', 'Belo Horizonte', 'Campo Grande'}
# 4

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4) # Duplicidade não gera erro é simplismente ignorado
print(s)

# Retorno:
# {1, 2, 3, 4}

# Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Retorno:
# {1, 2, 3}

# Forma 1
s.remove(3) # Não é índice informamos o valor removido
print(s)

# Retorno:
# {1, 2, 3}

# s.remove(33) # Caso o valor não seja encontrado no conjunto será retornodo em erro (KeyError)
# print(s)

# Retorno:
# KeyError: 33

# Forma 2

s.discard(2)
print(s)

# Retorno:
# {1}

s.discard(22) # Caso o valor não seja encontrado no conjunto nenhum erro é gerado
print(s)

# Retorno:
# {1}


# Copiando um conjunto para outro...

s = {1, 2, 3}
print(s)

# Retorno:
# {1, 2, 3}

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)
# Retorno:
# {1, 2, 3}

novo.add(4)

# Retorno:
# {1, 2, 3, 4}

print(novo)
print(s)

# Retorno:
# {1, 2, 3}

# Forma 2 - Shallow Copy

s = {1, 2, 3}
print(s)
novo = s

novo.add(4)

print(novo)
print(s)

# Retorno:
# {1, 2, 3}
# {1, 2, 3, 4}
# {1, 2, 3, 4}


# Podemos remover todos os itens de um conjunto

s = {1, 2, 3}
s.clear()
print(s)

# Retorno:
# set()


# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um contendo estudantes do curso de Java.

estaudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estaudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union (Mais recomendado; devido a visualização do código)

unicos = estaudantes_python.union((estaudantes_java))
print(unicos)

# Retono:
# {'Guilherme', 'Ellen', 'Patricia', 'Fernando', 'Pedro', 'Ana', 'Gustavo', 'Marcos', 'Julia'}

unicos1 = estaudantes_java.union((estaudantes_python))
print(unicos)

# Retono:
# {'Gustavo', 'Fernando', 'Julia', 'Pedro', 'Patricia', 'Ana', 'Guilherme', 'Marcos', 'Ellen'}

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estaudantes_python | estaudantes_java

# Retorno:
# {'Guilherme', 'Julia', 'Ana', 'Patricia', 'Ellen', 'Fernando', 'Gustavo', 'Marcos', 'Pedro'}


# Veja que alguns estudantes estão no conjunto de estudantes_python e também no conjunto de estudantes_java.

# Gerar um conjunto de estudantes que estão em ambos os conjuntos / cursos.

estaudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estaudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Forma 1 - Utilizando intersection

ambos1 = estaudantes_python.intersection(estaudantes_java)
print(ambos1)

# Retorno:
# {'Julia', 'Patricia'}

# Forma 2 - Utilizando o &
ambos2 = estaudantes_python&estaudantes_java
print(ambos2)

# Retorno:
# {'Julia', 'Patricia'}


# Métodos Matemáticos de Conjuntos

# Gerar um conjunto de estudantes que não estão no outro conjunto / curso.

estaudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estaudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

so_python = estaudantes_python.difference(estaudantes_java)
print(so_python)

# Retorno:
# {'Ellen', 'Marcos', 'Guilherme', 'Pedro'}

so_java = estaudantes_java.difference(estaudantes_python)
print(so_java)

# Retorno:
#{'Ana', 'Fernando', 'Gustavo'}


# Som*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais
s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

# Retorno:
# 21
# 6
# 1
# 6



s = {}
print(s)
print(type(s))

# Retorno:
# {}
# <class 'dict'>

print(dir(s))

# Retorno:
# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '
# getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '
# len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__',
# setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values']

"""










