"""
Módulo Collections - Default Dict

https://docs.python.org/3.9/library/collections.html#collections.defaultdict

# Recap Dicionários:

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

# print(dicionario['outro']) - 'Gera um KeyError: 'outro'


# Retorno:
# {'curso': 'Programação em Python: Essencial'}
# Programação em Python: Essencial
# KeyError: 'outro'

# Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar um lambda para
# isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar um achave que não
# existe, essa chave será criada e o valor default será atribuido.

"""
# OBS. Lambdas são funcções sem nome que podem ou não receber parâmetros de entrada e retornar valores.

# Fazer import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

# Retorno:
# defaultdict(<function <lambda> at 0x7fcab5f3f1f0>, {}) - Recebeu o valor vazio e é um dicionário

# Outro exemplo para evidênciar que o default - Dict cria um dicionário e assume o valor quando indicado, caso o
# a chave indicada ainda não existe no dicionário:

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

# Retorno:
# defaultdict(<function <lambda> at 0x7fb9a8a731f0>, {'curso': 'Programação em Python: Essencial'})

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não.

print(dicionario)

# Retorno:
# 0
# defaultdict(<function <lambda> at 0x7f9f149ba1f0>, {'curso': 'Programação em Python: Essencial', 'outro': 0})













