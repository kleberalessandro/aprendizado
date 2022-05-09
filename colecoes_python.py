
"""
##########             EXERCÍCIOS PYTHON - SEÇÃO 07 - PARTE 1           #############
"""

"""
1 - Faça um programa que possua um vetor denominados A que armezene 6 números inteiros. O programa deve executar os
seguintes passos:

(a) Atribuir os valores a esse vetor: 1, 0, 5, -2, -5, 7.

# Resolução - (a):
a = [1, 0, 5, -2, -5, 7]


(b) Armazenar em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1} e A[5] do vetor e mostre
na tela esta soma.

# Resolução - (b):
soma = sum([a[0], a[1], a[5]])
print(f' A soma dos dos valores das posiçõe A[0], A[1] e A[5] do vetor A = {soma}')


(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.

# Resolução - (c):
print(a)
a.pop(4)
print(a)
a.insert(4, 100)
print(a)


(d) Mostre na tela cada valor do vetor A, um em cada linha.

# Resolução - (d)
cont = 0
for valor in a:
    cont += 1
    print(f' Valor {cont} = {valor}')
"""

"""
2 - Crie um programa que Lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos

lista = []
cont = 0

while cont < 6:
    cont += 1
    valor = int(input(f'Informe um valor {cont}: '))
    lista.append(valor)
num1, num2, num3, num4, num5, num6 = lista
print(f'Os valores informados foram: num1 = {num1}, num2 = {num2}, num3 = {num3}, num4 = {num4}, num5 = {num5}, e '
      f'num6 = {num6}')
"""

"""
3 - Ler um conjnto de números reais, armazenado-o em vetor e calcular o quadrado dos componentes deste vetor,
armazenando o resultado em um outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

lista = []
lista_quadrado = []
cont = 0

while cont < 10:
    cont += 1
    valor = int(input(f'Informe um valor {cont}: '))
    quadrado = valor * 2
    lista.append(valor)
    lista_quadrado.append(quadrado)

for indice, lista in enumerate(lista):
    print(f' Indíce:{indice} o número informado foi: {lista}')

for indice, lista_quadrado in enumerate(lista_quadrado):
    print(f' Indíce:{indice} o quadrdo do número informado é :{lista_quadrado}')
"""

"""
4 - Faço um programa que leia um vetor de 8 posições e em seguida, leia também dois valores X e Y quaisquer
correspondentes as duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas
respectivas posições X e Y.

vetor8 = []
cont = 0

while cont <= 7:
    cont += 1
    pos = int(input(f'Informe o valor da posição {cont}: '))
    vetor8.append(pos)

x = vetor8[0]
y = vetor8[1]
somaX_Y = x + y

print(f'O vetor de 8 posições = {vetor8} digito que corresponde a posição X = {x} e Y = {y} e X + Y = {somaX_Y}')
"""

"""
5- Leia um vetor de 10 posições. Contar e escrever contar e escrever quantos valores pares ele possui.

vetor_10 = []
vetor_par = []
cont = 0

while cont <= 9:
    cont += 1
    pos = int(input(f'Informe o valor da posição {cont}: '))
    vetor_10.append(pos)
    if pos % 2 == 0:
        vetor_par.append(pos)
qtd = len(vetor_par)

print(f'Para o vetor de 10 posições foram digitadas os valores: {vetor_10}, que contem os valores pares:{vetor_par},'
      f'contendo {qtd} valores pares.')

"""

""""
6 - Faça um programa que receba do usuário um vetor de 10 posições. Em seguida deverá ser impresso o maior e o menor
elemento do vetor.

vetor_10 = []
cont = 0

while cont <= 9:
    cont += 1
    pos = int(input(f'Informe o valor da posição {cont} para o vetor: '))
    vetor_10.append(pos)


print(f'O vetor de 10 posições recebeu os valores {vetor_10} o maior valor recebido foi: {max(vetor_10)} e o menor foi: '
      f'{min(vetor_10)}')

"""


"""
7 - Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a 
posição que ele se encontra.

vetor_10 = []
cont = -1
lista_indice = []

while cont <= 8:
    cont += 1
    valor = (int(input(f'Informe um valor para a posição {cont} do vetor de 10 posições: ')))
    vetor_10.append(valor)
    maior = max(vetor_10)
    for valor, indice in enumerate(vetor_10):
        indice = (indice)
    lista_indice.append(indice)
    indice_maior = max(lista_indice)


print(f'Para o vetor de 10 posições foram informados 0e elementos: {vetor_10} e o maior elemento encontrado foi:{maior}'
      f'seu indice correponde a posição {indice_maior}')
"""


""""
8 - Crie um programa que lê 6 valores inteiros, em seguida, mostre na tela os valores lidos na ordem inversa.

lista = []
lista1 = []
cont = 0

while cont <= 5:
    cont += 1
    valor = int(input(f'Informe o valor {cont} da lista:'))
    lista.append(valor)
print(lista)
lista1 = lista[::-1]
print(f'Os valores informados para a lista de 6 valores inteiros foi ={lista} e a ordem inversa ={lista1}')
"""


"""
9 - Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.


lista = []
lista1 = []
cont = 0

while cont < 6:
    valor = int(input(f'Informe um valor par inteiro: '))
    if valor % 2 == 0 and valor > 0:
        cont += 1
        lista.append(valor)

    else:
        print(f'O valor {valor} informado não é par. Favor Informar um número inteiro par!!')

lista1 = lista.copy()
lista1.reverse()

print(f' Os valores informados para a lista foram na seguinte ordem: {lista} e a inversão dos mesmos fica : {lista1}')

"""



"""
11 - Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números begativos e a
soma de números dos números positivos desse vetor.

lista = []
cont = 0
negativo = []
positivo = []

while cont < 10:
    cont += 1
    valor = int(input(f'Informe um valor real {cont}/10: '))
    lista.append(valor)
    if valor < 0:
        negativo.append(valor)
    else:
        positivo.append(valor)

negativo = len(negativo)
positivo = sum(positivo)

print(f'Para o vetor de 10 posições foram infomados os elementos:{lista} sendo {negativo} valores negativos e a soma '
      f'dos elementos positivos = {positivo}.')
"""


"""
11 - Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.

from statistics import mean

lista = []
cont = 0

while cont < 15:
    cont += 1
    nota = int(input(f'Informe a nota do aluno {cont}/15: '))
    lista.append(nota)
media = statistics.mean(lista)

print(f'As notas informadas foram: {lista} e a média destas notas = {media}')
"""



"""
13 - Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se incotram o maior e o menor valor.

lista = []
cont = 0

while cont < 5:
    cont += 1
    valor = int(input(f'Informe o valor {cont}/5: '))
    lista.append(valor)
    maior = max(lista)
    menor = min(lista)
    indice_maior = lista.index(max(lista))
    indice_menor = lista.index((min(lista)))

print(f'Os valores informados foram: {lista} e o maior valor é {maior} que está na posição {indice_maior} e o menor '
      f'valor da lista é {menor} e está na posição {indice_menor}.')
"""


"""
14 - Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva 
na tela.

from collections import Counter

vetor_10 = []
elementos = []
cont = 0

while cont < 10:
    cont += 1
    valor = int(input(f'Informe o valor {cont}/10: '))
    vetor_10.append(valor)
    elementos.append(valor)
vetor_10 = Counter(vetor_10)

for chave, valor in vetor_10.items():
    if valor > 1:
        print(f'O valor {chave} foi repetido {valor} vezes')
vetor_10 = sorted(elementos)

print(f'Todos os 10 números digitados foram:{elementos}')
"""


"""
15 - Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.

from collections import Counter

lista = []
cont = 0
nao_repetidos = []

while cont < 20:
    cont += 1
    elementos = int(input(f'Informe o valor {cont}/20: '))
    if elementos >= 0:
        lista.append(elementos)
    else:
        print(f'!!!O número informado deve ser inteiro e positivo!!!'.upper())
        cont -= 1
lista1 = Counter(lista)
for chave, valor in lista1.items():
    if valor > 1:
        del chave
    else:
        nao_repetidos.append(chave)

print(f' Os digitados correspondentes ao vetor solicitado foram:{lista} e os números que não repetem são:{nao_repetidos}')

"""



"""
16 - Faça um programa que leia um vetor de 5 posições para números reais, e, depois um código inteiro. Se o código for 
zero, finalize o programa; se for 1, mostre o vetor na ordem direita; se for 2 mostre o vetor na ordem inversa. Caso, o
código for de 1 e 2 escreva uma mensagem informando que o código é inválido.


lista = []
cont = 0

while cont < 5:
    cont += 1
    vetor_5 = input(f'Informe um número real {cont}/5: ')
    lista.append(vetor_5)

print('0 = Finalizar o Programa\n'
      '1 = Mostrar o vetor será retornado na ordem direta\n'
      '2 = Mostrar o vetor será retornado na ordem inversa\n'
      'Outros = Código Inválido')

codigo = int(input('Informe uma das opções descritas acima: '.upper()))
if codigo == 1:
    print(f'Os valores informado em suas respectivas ordem foram:{lista}')
elif codigo == 2:
    print(f'Os valores informado em ordem inversa foram:{lista[::-1]}')
elif codigo == 0:
    print('!!!Programa Finalizado!!!'.upper())
else:
    print('!!!Código Informado é Inválido!!!'.upper())
"""


"""
17 - Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuem valores negativos.

lista = []
lista1 = []
cont = 0

while cont < 10:
    cont += 1
    valor = int(input('Informe um valor real: '))
    lista.append(valor)
    if valor < 0:
        valor = 0
        lista1.append(valor)
    else:
        lista1.append(valor)


print(f' Os valores digitados foram:{lista} e a lista alterada ficou assim: {lista1}')
"""



"""
18 - Faça um programa que leia um vetor de 10 números x. Conte os múltiplos de um número inteiro x num vetor e mostre-os
na tela.


                                    ???????????????????????????????
"""

"""
19 - Faum vetor de tamanho 50 preenchendo com o seguinte valor: (i + 5) % (i + 1), sendo i a posição do elemento no 
vetor. Em seguida imprima e mostre na tela.


                                    ???????????????????????????????
"""

"""
20 - Escreva um programa que leia números inteiros [0,50] e os armazene em um vetor com 10 posições. Preencha um segundo
vetor apenas com os números ímpares do primeiro vetor. Imprima os dois vetores, 2 elemento por linha.

vetor = []
qtd = 10
cont = 0
impares = []

while cont < 10:
    cont += 1
    numero = int(input(f'Informe o número {cont}/10: '))
    if numero >= 0 and numero <= 50:
        vetor.append(numero)
        if numero % 2 == 1:
            impares.append(numero)
    else:
        cont -= 1
        print('Deve ser informado um número entre 0 e 50'.upper())

print(f'O primeiro vetor corresponde aos números digitados:{vetor} e o segundo vetor correspondentes aos números\n'
      f'impares são:{impares}')
"""

"""
21 - Faça um programa que receba do usuário dois vetores A e B, com 10 números inteiros cada. Crie um novo vetor 
determinador C = A - B. Mostre na tela os dados do vetor C.

vetor_A = set()
cont_A = 0

vetor_B = set()
cont_B = 0

determinador_C = set()

while cont_A < 10:
    cont_A += 1
    valor_A = input(f"Informe o valor {cont_A}/10 do vetor 'A': ")
    vetor_A.add(valor_A)


while cont_B < 10:
    cont_B += 1
    valor_B = input(f"Informe o valor {cont_B}/10 do vetor 'B': ")
    vetor_B.add(valor_B)

determinador_C = vetor_A.union(vetor_B)


print(f"O vetor 'A' recebeu os dados:{vetor_A}\n"
      f"e o vetor 'B':{vetor_B} \n"
      f"sendo assim o vetor determonador 'C' = 'A' - 'B' ficou com os dados:{determinador_C}")

"""



"""
22 - Faça um programa que leia dois vetores de 10 posições e calcule outro vetor, nas posições pares os valores do
primeiro e nas e nas posições impares os valores do segundo.

vetor_1 = []
vetor_2 = []
vetor_3 = []
cont = 0

while cont < 10:
    cont += 1
    primeiro = input(f'Informe o valor {cont}/10 do primeiro vetor: ')
    segundo = input(f'Informe o valor {cont}/10 do segundo vetor: ')
    vetor_1.append(primeiro)
    vetor_1.append(segundo)
tupla = tuple(vetor_1)

for indice, valor in enumerate(tupla):

    print(f'Indice:{indice} valor:{valor}')
"""


"""
23 - Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles. Os 
conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar é dado por:
x1 * x2 + x2 * y2 +....xn + yn.

vetor_1 = []
vetor_2 = []
cont = 0
soma_produtos = []

while cont < 5:
    cont += 1
    conjuto_1 = int(input(f'Informe o n.{cont}/10 do primeiro vetor: '))
    conjunto_2 = int(input(f'Informe o n.{cont}/10) do segundo vetor: '))

    vetor_1.append(conjuto_1)
    vetor_2.append(conjunto_2)
    produto = conjuto_1 * conjunto_2
    soma_produtos.append(produto)

print(vetor_1)
print(vetor_2)
print(soma_produtos)
soma_produtos = sum(soma_produtos)
print(f'O produto escalar dos dois conjuntoa é = {soma_produtos}')
"""


"""
24 - Faça um proguama que leia dez conjuntos de dois valores, o primeiro representa o número do aluno e o segundo 
representando a sua altura em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número do aluno mais baixo e 
do mais alto, juntamente com sua alturas.

import operator

alunos = []
altura = []
cont = 0

for n in range(1, 11):
    numero_aluno = int(input(f'Informe o número do aluno {n}/10: '))
    altura_aluno = input(f'Informe a altura do aluno {numero_aluno}: ')
    alunos.append(numero_aluno)
    altura.append(altura_aluno)

dic_aluno = dict(zip(alunos, altura))

# O Aluno mais Baixo:
print(f"O número do aluno mais baixo é: {(min(dic_aluno.items(), key=operator.itemgetter(1))[0])} e sua altura é:"
      f"{(dic_aluno[min(dic_aluno,key=dic_aluno.get)])}")

# O Aluno mais Alto:
print(f"O número do aluno mais alto é:{(max(dic_aluno.items(), key=operator.itemgetter(1))[0])} e sua altura é:"
      f"{(dic_aluno[max(dic_aluno,key=dic_aluno.get)])}")
"""


"""
25 - Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não são multiplos de 7 ou
terminam com 7.


vetor_100 = []


for n in range(0, 130):
    vetor_100.append(n)
    if n % 7 == 0 or str(n)[-1] == '7':
        vetor_100.remove(n)

print(len(vetor_100))
print(vetor_100)
"""


"""
26 - Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números, onde m é a média do vetor.

desvio padrão = raiz(1/n-1) n somatório i=1 ) (v[i] - m)²

                            ??????????????????????????????????????????????
"""



"""
27 - Leia 10 números inteiros e armazena em um vetor. Em seguida escreva os elementos que são primos e suas respectivas
posições no vetor.

                            ?????????????????????????????
"""

"""
28 - Leia 10 números e armazene em um vetor v. Crie novos vetores v1 e v2. Copie os valores ímpares de v para v1, e os
pares para v2. Note que cada um dos vetores v1 e v2 têm no máximo 10 elementos, mas nem todos são utilizados. No final
escreva os elementos UTILIZADOS de v1 e v2.

v = []
v1 = []
v2 = []
cont = 0
while len(v) < 10:
    cont += 1
    numeros = int(input(f'Informe o número {cont}/10: '))
    v.append(numeros)
    if numeros % 2 == 1:
        v1.append(numeros)
    elif numeros % 2 == 0:
        v2.append(numeros)
    else:
        print(f'O dado informa {numeros} não atende ao solicitado (número)'.upper())
        cont -= 1

print(f'Dados utilizados:\n'
      f'Impar: {v1[0], v1[1], v1[2]}\n'
      f'Par:{v2[0], v2[1],v2[2]}')
"""


"""
29 - Faça um programa que receba 6 números inteiros e mostre:
    -   Os números pares digitados;
    -   A soma dos números pares digitados;
    -   Os números ímpares digitados;
    -   A quantidade de números ímpares digitados;
    
    
vetor_6 = []
pares = []
impares = []
cont = 0

while len(vetor_6) < 6:
    cont += 1
    numeros = int(input(f'Informe o número {cont}/6: '))
    vetor_6.append(numeros)

    if numeros % 2 == 0:
        pares.append(numeros)

    elif numeros % 2 == 1:
        impares.append(numeros)

    else:
        print(f'O dados digitado {numeros} não atende a solicitação'.upper())
        cont -= 1
print(f'Os dados digitados foram: {vetor_6}.\n'
      f'Os números pares digitados foram: {pares}.\n'
      f'A soma dos números pares digitados é = {sum(pares)}.\n'
      f'Os números ímpares digitados foram: {impares}.\n'
      f'A quantidade de números ímpares digitados é = {len(impares)}.')

"""


"""
30 - Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os 2 vetores
anteriores, ou seja que contém apenas os números que estão em ambos os vetores. Não deve conter número repetidos.


vetor_1 = []
vetor_2 = []
interseccao = []
cont = 0

while len(vetor_1) < 10:
    cont += 1
    numero = int(input(f'Informe para o 1º vetor o número {cont}/10: '))
    vetor_1.append(numero)

cont = 0
while len(vetor_2) < 10:
    cont += 1
    numero1 = int(input(f'Informe para o 2º vetor o número {cont}/10: '))
    vetor_2.append(numero1)

for n in vetor_1:
    if n in vetor_2:
        interseccao.append(n)
interseccao = set(interseccao)

print(f'Os números digitados no 1ª vetor são:{vetor_1}.\n'
      f'Os números digitados no 2º vetor são:{vetor_2}.\n'
      f'O os números digitados nos dois vetores foi:{interseccao}.'.upper())
"""



"""
31 - Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união entre os 2 vetores 
anteriores, ou seja, que contém os números dos dois vetores. Não deve conter números repetidos.

vetor_1 = []
vetor_2 = []
conjunto = []
cont = 0

while len(vetor_1) < 10:
    numeros = int(input(f'Informe o número {cont}/10 do 1º vetor: '))
    vetor_1.append(numeros)

cont = 0
while len(vetor_2) < 10:
    numeros = int(input(f' Informe o número {cont}/10 do 2º vetor: '))
    vetor_2.append(numeros)

conjunto = vetor_1 + vetor_2
conjunto = set(conjunto)

print(f'O 1º vetor recebeu os números:{vetor_1}.\n'
      f'O 2º vetor recebeu os números:{vetor_2}.\n'
      f'O vetor correspondente a união sem repetição é:{conjunto}.')

"""


"""
32 - Leia dois vetores de inteiros x e y cada um com 5 elementos (assuma que o usuário não informa elementos repetidos).
Calcule e mostre os vetores resultantes em cada caso abaixo:
 
 - Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y.
 - Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma posição y.
 - Diferença entre x e y: todos os elementos de x que não existam em y.
 - Intersecção entre x e y: apenas os elementos que aparecem nos dois vetores.
 - União entre x e y: todos os elementos de x, e todos os elementos de y que não estão em x.


vetor_x = []
vetor_y = []
lista_soma = []
lista_produto = []
elementos_so_x = set()
interseccao = set()
uniao_x_y = set()
cont = 0

while len(vetor_x) < 5:
    cont += 1
    elem_x = int(input(f'Informe o elemento {cont}/5 do vetor_x:'))
    if elem_x in vetor_x:
        print(f'O elemento {elem_x} digitado já existe na lista. FAVOR INFORMAR OUTRO ELEMENTO')
        cont -= 1
    else:
        vetor_x.append(elem_x)

cont = 0
while len(vetor_y) < 5:
    cont += 1
    elem_y = int(input(f'Informe o elemento {cont}/5 do vetor_y:'))
    if elem_y in vetor_y:
        print(f'O elemento {elem_y} digitado já existe na lista. FAVOR INFORMAR OUTRO ELEMENTO')
        cont -= 1
    else:
        vetor_y.append(elem_y)

cont = -1
while cont < 4:
    cont += 1
    soma = (vetor_x[cont]) + (vetor_y[cont])
    produto = (vetor_x[cont]) * (vetor_y[cont])
    lista_soma.append(soma)
    lista_produto.append(produto)
    conjunto_x = set(vetor_x)
    conjunto_y = set(vetor_y)
    diferenca = conjunto_x.difference(conjunto_y)
    interseccao = conjunto_x.intersection(conjunto_y)
    uniao_x_y = conjunto_x.union(conjunto_y)

print(f'Os valores digitados para o vetor x foram:{vetor_x} e para o vetor y foram:{vetor_y}')

print(f'A Soma de cada elemento de x com o elemento da mesma posição em y é = {lista_soma}')

print(f'A multiplicação de cada elemento de x com o elemento da mesma posição y é = {lista_produto}')

print(f'Todos os elementos de x que não existam em y é = {diferenca}')

print(f'A apenas os elementos que aparecem nos dois vetores é = {interseccao}')

print(f'Todos os elementos de x, e todos os elementos de y que não estão em x é = {uniao_x_y}')

"""



"""
33 - Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimne as posições com valores zero.
Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para trás no vetor.


vetor_15 = []
cont = 0

while cont <= 15:
    cont += 1
    num = int(input(f'Informe o número {cont}/15: '))
    vetor_15.append(num)

vetor_15_zero = vetor_15

for n in vetor_15_zero:
    if n == 0:
        vetor_15_zero.remove(n)

print(f'Para o vetor de 15 posições foram digitados os seguintes valores:{vetor_15}\n'
      f'O vetor compactado ficou com os valores:{vetor_15_zero}')
"""



"""
34 - Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor. Os dados deverão ser armazenados
no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite um número que já foi digitado anteriomente, o
programa deverá pedir para ele digitar outro número. Note que cada valor digitado pelo usuário deve ser pesquisado no
vetor, verificando se ele existe entre os números que já foram fornecidos. Exibir na tela o vetor final que foi digitado.

vetor_10 = []
cont = 0

while len(vetor_10) < 10:
    cont += 1
    num = int(input(f'informe o número {cont}/10: '))
    if num in vetor_10:
        print(f'O número {num} já foi digirado; FAVOR INFORMAR OUTRO NÚMERO!!')
        cont -= 1
    else:
        vetor_10.append(num)
print(f'Os números fornecido sem repetição foram:{vetor_10}')
"""


"""
35 - Faça um programa que leia dois números a e b mas (positivos menores que 10_000) e:

    -   Crie um vetor onde cada posição é um algarismo do número. A primeira posição é o algarismo menos signifitivo;
    -   Crie um vetor que seja a soma de a e b mas faça-o usando apenas os vetores construídos anteriormente.

Dica: Some as posições correspondentes. Se a soma ultrapassar 10, subtraia 10 do resultado e some 1 à próxima posição.

                          ????????????????????????????????????????????
"""



"""
36 - Leia um vetor com 10 números reais, ordene os elementos deste vetor, e no final escreva os elementos do vetor 
ordenado.

vetor_10 = []
cont = 0

while len(vetor_10) < 10:
    cont += 1
    num = (input(f' Informe o núemro {cont}/10: '))
    vetor_10.append(num)

vetor_10.sort(key=float)

print(vetor_10)
"""


"""
37 - Considere um vetor A com 11 elementos onde A1 < A2 ...A6 > A7 > A8 >...> A11, ou seja, está ordenado em ordem 
crescente até os exto elemento, e a partir desse elemento está ordenado em ordem decrescente. Dado o vetor da questão
anterior, proponham um algoritmo para ordenar os elementos.

from natsort import natsorted

a = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a11', 'a10', 'a9', 'a8', 'a7']
print(type(a))
print(natsorted(a))
"""



"""
38 - Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores, guardando-os num 
vetor. Ordene o valor assim que ele for digitado. Mostre ao final na tela os valores em ordem.

lista_numeros = []
cont = 0

while len(lista_numeros) < 10:
    cont += 1
    numero = float(input(f'Informe o número {cont}/10: '))
    lista_numeros.append(numero)
    lista_numeros.sort()

print(lista_numeros)
"""



"""
39 - Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triangulo de 
Pascal:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
...

                            ??????????????   ???????????????????????????????????
"""



















