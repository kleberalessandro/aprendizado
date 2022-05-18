"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o itervel está vazio


"""

# Exemplo all():

print(all([0, 1, 2, 3, 4])) # Lista é False pois o zero é igual a False então nenm todos os elementos são True
# Retorno / Saída;
# False

print(all([1, 2, 3, 4])) # Todos os números são verdadeiros? Então a lista é True
# Retorno / Saída;
# True

print(all([])) # Lista True pois a lista está vazia.
# Retorno / Saída;
# True

print(all([1, 2, 3, 4])) # Tupla igual a True pois todos os números são verdadeiros.
# Retorno / Saída;
# True

print(all({1, 2, 3, 4})) # Set igual a True pois todos os números são verdadeiros.
# Retorno / Saída;
# True

print(all('Geek')) # String igual a verdadeiro pois todos são veradeiros
# Retorno / Saída;
# True

nomes = ['Carlos', 'Camila', 'Carla', 'Cristina']

print(all(nome[0] == 'C' for nome in nomes))
# Retorno / Saída;
# True

nomes = ['Carlos', 'Camila', 'Carla', 'Cristina', 'Daniel']
print(all(nome[0] == 'C' for nome in nomes))
# Retorno / Saída;
# False

print(all([letra for letra in 'eio' if letra in 'aeiou'])) # Ficar esperto pois se a lista também vier vazio ele
                                                            # considera True ou seja se nenhuma letra estiver então vai
                                                            # ser vazio.
# Retorno / Saída;
# True


print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
# Retorno / Saída;
# True

# any() -> Retorno True se qualquer elemen do iterável for verdadeiro. Se o iterável estiver vazio. retorna False.

print(any([0, 1, 2, 3, 4])) # True
# Retorno / Saída;
# True

print(any([0, False, {}, (), []])) # False [False pois todos os elemento da lista são False]
# Retorno / Saída;
# False

nomes = ['Carlos', 'Camila', 'Carla', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))
# Retorno / Saída;
# True

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
# Retorno / Saída;
# True













