"""
Dicionários:

OBS. Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave / valor.

Dicionários são representados por chaves {}.

print(type({}))

# Retorno:
# <class 'dict'>

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor '
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;


# Criação de dicionários
# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Retorno:
# {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# <class 'dict'>

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Retorno:
# {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# <class 'dict'>


# Acessando elementos

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}


# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
# print(paises['ru']) - Caso tentamos fazer um acesso utilizando uma chave que não exista, teremos o erro KeyError

# Retorno:
# Brasil
# Paraguai

# Fornma 2 - Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('py'))
print(paises.get('ru')) # Desta forma não tendo a chave retorno como None e não KeyError

# Retorno:
# Brasil
# Paraguai
# None

# Outro Exemplo de aplicação do None:

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('py')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Retorno:
# Encontrei o país Paraguai

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')


# Mais um exemplo de aplicação do None com uso de 'get':


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('ru', 'Não encontrado') # OBS: Podemos definir um valor padrão para caso não encontremos o objeto
print(f' Encontrei o pais: {pais}')       # com a chave informada

# Retorno:
# Encontrei o pais: Não encontrado

pais = paises.get('py', 'Não encontrado')
print(f' Encontrei o pais: {pais}')

# Retorno:
# Encontrei o pais: Paraguai


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos verificar se deteminada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

# Retorno:
# True
# False
# False

if 'ru' in paises:
    russia = paises['ru'] # Caso não contenha a chave o programa não fará nada inclusive não retorno erro


Podemos utilizar qualque tipo de dado (int, float, string, boolean) inclusive lista, tupla dicionário, como chave
# de dicionários.

# OBS: Tuplas por exemplo são bastante utilizadas como chaves de dicionários pois as mesmas são imutável no exemplo foi
# dado uma localização
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Retorno:
# {(35.6895, 39.6917): 'Escritório em Tókio', (40.7128, 74.006): 'Escritório em Nova York', (37.7749, 122.4194):
# 'Escritório em São Paulo'}
# <class 'dict'>



# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Retorno:
# {'jan': 100, 'fev': 120, 'mar': 300}
# <class 'dict'>

# Forma 1 - Mais comum
receita['abr'] = 350
print(receita)
print(type(receita))

# Retorno:
# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350}
# <class 'dict'>

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)
print(type(receita))

# Retorno:
# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 500}
# <class 'dict'>

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 500
print(receita)

# Retorno:
# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 500}


# Forma 2

receita.update(({'mai': 600}))

print(receita)

# Retorno:
# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 600}


# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.



# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)

print(receita)

# Retorno:
# {'jan': 100, 'fev': 120, 'mar': 300}
# 300
# {'jan': 100, 'fev': 120}

# OBS1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma2

del receita['fev']

print(receita)

# Retorno:
# {'jan': 100}

# del receita['fev']
# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.
"""

# Imagine que você têm um comercio eletrônico onde tem um carrinho de compras no qual adicionamos produtos.
"""
Carrinho de Compras:
    Produto 1:
        - nome
        - quantidade
        - preço
    Produto 2:
        - nome
        - quantidade
        - preço
        

# Forma 1: - Proderiamos utilizar uma lista para isso? Sim

carrinho = []
produto1 = ['Playstation 4', 1, 2_300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Retorno;
# [['Playstation 4', 1, 2300.0], ['God of War 4', 1, 150.0]]

# Usando Lista: Teriamos que saber qual é o índice de cada informação no produto.

# Forma 2: - Poderiamos utilizar uma tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2_300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

# Retorno:
# (('Playstation 4', 1, 2300.0), ('God of War 4', 1, 150.0))

# Usando Tuplas: Tabém teriamos que saber qual é o índice de cada informação no produto.


# Forma 3: - Poderiamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2_300.00}
produto2 = {'nome': 'God of War 4', 'quantiadde': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Retorno:
# [{'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.0}, {'nome': 'God of War 4', 'quantiadde': 1,
# 'preço': 150.0}]

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza sobre
# cada informação.


# Métodos de dicionários:
"""
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__'
'getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__',
'__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
'setdefault', 'update', 'values']
"""
# Alguns deles:
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Retorno:
# {'a': 1, 'b': 2, 'c': 3}
# <class 'dict'>

# Limpar o dicionário (Zerar dados):
d.clear()
print(d)

# Retorno:
# {} - Vazio ou seja zerado

 Copiando um dicionário para outro:

# Forma 1 - Deep Copy

d = dict(a=1, b=2, c=3)
novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Retorno:
# {'a': 1, 'b': 2, 'c': 3}
# {'a': 1, 'b': 2, 'c': 3}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4} - Deep Copy



# Forma 2 - Shallow Copy ( Altera os dois )

d = dict(a=1, b=2, c=3)
print(d)

novo = d
print(d)
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Retorno:
# {'a': 1, 'b': 2, 'c': 3}
# {'a': 1, 'b': 2, 'c': 3}
# {'a': 1, 'b': 2, 'c': 3}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4} - Shallow Copy
# {'a': 1, 'b': 2, 'c': 3, 'd': 4} - Shallow Copy


# Forma não usual de criação de dicionários:

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

# Retorno:
# {'a': 'b'}
# <class 'dict'>

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# Retorno:
# {'nome': 'desconhecido', 'pontos': 'desconhecido', 'email': 'desconhecido', 'profile': 'desconhecido'}
# <class 'dict'>

'OBS: O método fromkeys recebe dois parâmetros: um interável e um valor.' \
'Ele vai gerar para cada valor de iterável uma chave e irá atribuir a esta chave o valor informado.'

veja = {}.fromkeys('teste', 'valor')
print(veja)

# Retorno:
# {'t': 'valor', 'e': 'valor', 's': 'valor'} - Para cada letra ele absolveu o valor e não repetiu as letras

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

# Retorno:
# {1: 'novo', 2: 'novo', 3: 'novo', 4: 'novo', 5: 'novo', 6: 'novo', 7: 'novo', 8: 'novo', 9: 'novo', 10: 'novo'}

"""






