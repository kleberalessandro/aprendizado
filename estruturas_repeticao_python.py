"""
1- Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0.
"""

"""
2 - Escreva um programa que escreva na tela, 1 até 100, de 1 em 1, 3 vezes. A primira vez deve usar a estrutura de 
repetição for, a segunda while, e a tereceira do while.

for numero in range(1, 101):
    print(numero,end=' ')

numero1 = -1
while numero1 < 100:
    numero1 = numero1 + 1
    print(numero1)

numero2 = -1
while numero2 < 100:
    numero2 = numero2 + 1
    print(numero2, end=' ')
"""
"""
3 - Faça um algoritimo utilizando o comando while que mostre uma contagem regressiva na tela, iniciando em 10 e termine
em 0. Mostra uma mensagem "Fim!" após a contagem. 

numero = 10

while numero > 0 and numero < 11:
    numero = numero - 1
    print(numero, end=' ')
print('\n''Fim!')
"""
"""
4 - Escreva um programa que desclare um inteiro, inicialize-o com 0, e incremente-o de 1000 em 1000, imprimindo seu
valor na tela, até que seu valor seja 1_000_000(cem mil).

for num in range(0, 1_000_000, 1_000):
    #numero = int(num)
    print(num)
    print(type(num))
"""
"""
5 - Faça um programa que peça ao usuário para digitar 10 valores e some-os.

qtd = 10
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe 10 valores diferentes até completar {n}/{qtd}: '))
    soma = num + soma
    print(soma)
"""

"""
6 - Faça um programa que leia 10 inteiros e imprima a média:

qtd = 10
soma = 0

for n in range(1, qtd+1):
    num = int(input('Informe 10 valores diferentes para cálculo da média: '))
    soma = num + soma
    media = int(soma / qtd)
    print(soma)
print(f'A média dos {qtd} valores informados é {media}')
"""
"""
7 - Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.

qtd = 10
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o valor: '))
    if num > 0:
        soma = num + soma
        media = int(soma / qtd)
        print(f'O número {n} de {qtd} digitado foi {num} e é positivo!!')
    else:
        pass
print(f'A média dos {qtd} valores positivos informados é = {media}')
"""

"""
8 - Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

numeros = []

for n in range(1, 11):
    numeros.append(int(input(f'Informe o valor: ')))
print(f'O maior número é {max(numeros)}')
print(f'O meno número é {min(numeros)}')
"""

"""
9 - Faça um programa que leia um número N e depois imprima os N primeiros números naturais impares.


numero = int(input(f'Informe o número: '))
if numero > 0 and numero % 2 == 1:
    for n in range(1, numero+numero, 2):
        print(n, 'impar')
elif numero > 0 and numero % 2 == 0:
    for n in range(1, numero+numero, 2):
        print(n, 'par')
else:
    print('DADOS INFORMADOS NÃO ATENDE A REGRA ESTABELECIDA!!')
"""

"""
10 - Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.


qtd = 0
lista = []
lista1 = []

while qtd == 0:
    lista = list(range(0, 100, 2))
    print(len(lista))
    lista1 = sum(lista[1:50])
    qtd += 1
    print(lista1)
"""

"""
11 - Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de até N em ordem 
crescente.

num = int(input('Informe o número desejado: '))

for n in range(0, num+1):
    print(n, end=', ')
"""

"""
12 - Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de até N em ordem 
decrescente.

num = int(input('Informe o número desejado: '))

for n in range(num, -1, -1):
    print(n, end=', ')
"""

"""
13 - Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
crescente.

num = int(input('Informe o número inteiro par positivo: '))
if num > 0:
    for n in range(0, num+1, 2):
        if num % 2 == 0:
            print(n, end=', ')
        else:
            print(f' O número informado foi {num}', 'O REQUISITO É UM NÚMERO PAR')
            break
else:
    print(f' O número informado foi {num}', 'O REQUISITO É UM NÚMERO PAR e POSITIVO')
"""

"""
14 - Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
decrescente.

num = int(input('Informe o número inteiro par positivo: '))

if num >= 0 and num % 2 == 0:
    for n in range (num, -1, -1):
        print(n, end=', ')
else:
    print(f' O número informado foi {num}','- O REQUISITO É UM NÚMERO PAR e POSITIVO')
"""

"""
15 - Faça um programa que leia um número inteiro positivo impar N e imprima todos os números ímpares de 1 até N em 
ordem crescente


num = int(input('Informe o número inteiro impar positivo: '))

if num >= 1 and num % 2 == 1:
    for n in range(1, num+2, 2):
        print(n,end=', ')
else:
    print('INFORME UM NÚMERO INTEIRO, POSITIVO E IMPAR!!!')
"""

"""
16 - Faça um programa que leia um número inteiro positivo impar N e imprima todos os números ímpares de 1 até N em ordem
decrescente.

num = int(input('Informe um número inteiro, positivo e impar: '))

if num >= 1 and num % 2 == 1:
    for n in range(num, 0, -2):
        print(n,end=' ')
else:
    print('INFORME UM NÚMERO INTEIRO, POSITIVO E IMPAR!!!')
"""
"""
17 - Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais.

n = int(input('Informe um número inteiro positivo: '))
soma = 0

if n >= 0:
    for num in range(0, n+1):
        soma += num
    print(f'A o número inteiro digitado foi {n} e a soma dos {n} primeiros numeros naturais é = {soma}')
else:
    print('NUMERO DEVE SER INFORMADO COMO INTEIRO E POSITIVO!!!!!')
"""

"""
18 - Escreva um algoritimo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número
foi lido. A quantidade de números a serem lidos deve ser fornecido pelo usuário.

qtd_numeros = int(input('Quantos números devem ser lidos? '))
lista = list()
cont = 0

while cont < qtd_numeros:
    cont += 1
    numero = (input('Informe o número a ser lido: '))

    lista.append(numero)

maior = max(lista)
menor = min(lista)
qtd_maior = lista.count(maior)

lista.sort()

print(f' O maior número da lista é: {maior} e foi digitado: {qtd_maior} vezes na lista {lista}.')
"""

"""
19 - Escreva um algoritimo que leia um número inteiro entre 100 e 999 e imprima na saída um dos algarismos que compóem
o número. 

num = int(input(' Informe um número entre 100 e 999: '))


if num >= 100 and num <= 999:
    num = str(num)
    num1 = num[1]
    print(f' O número digitado foi {num} e o um dos algarismo que compõem o número digitado é {num1}')

else:
    print(f'O NÚMERO DIGITADO FOI {num} E NÃO ATENDE A REGRA ESTABELECIDA!!!')
"""

"""
20 - Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados
lidos e números de valores pares. O precesso termina quando for digitado o número 1000.

num = 0
par = impar = 0
qtd_num = 0
lista = list()

while num != 1_000:
    num = int(input('Informe um número inteiro da sequência (Para quando digitar 1000): '))
    if num == 1_000:
        print(f'O numero digitado foi {num} para PARAR !!!')
    elif num > 0 and num < 1_000:
        lista1 = lista.append(num)
        qtd_num += 1
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
            print(f'!!!!!!!!!!!!O NÚMERO {num} DIGITADO NÃO É PAR!!!!!!!!!!!!!')
lista.sort()
print(f'A sequencia de números digitados foi {lista} totalizando {qtd_num} números digitados sendo destes {par} '
      f'par e {impar} impar.')

if num < 0 and num > 1000:
    print(' O NÚMERO DIGITADO NÃO ATENDE A REGRA ESTABELECIDA NO ENUNCIONADO!!!!')
"""

"""
21 - Faça um programa que receba dois números. Clacule e mostre:
    A soma dos números pares desse intervalo de números, incluindo os digitados;
    A multiplicação dos números impares desse intervalo, incluindo os digitados

import numpy as np

num = int(input('Informe o primeiro número: '))
num1 = int(input('Inform o segundo numero: '))
lista_soma = []
soma = []
lista_mult = []
mult = []
if num < num1:
    for n in range (num, num1+1):
        if n % 2 == 0:
            lista_soma = soma.append(n)
            lista_soma = sum(soma)

    for n in range (num, num1+1):
        if n % 2 == 1:
            lista_mult = mult.append(n)
            lista_mult = np.prod(np.array(mult))

    print(f'O 1º número digitado foi {num} e o 2º foi {num1} sendo assim os elementos pares do intervalo são: {soma} e '
          f'a soma dos mesmos = {lista_soma:.2f} \n'
          f'Os elementos impares são {mult} e a multiplicação dos mesmos é = {lista_mult:.2f}')
else:
    print('O PRIMEIRO NÚMERO DEVE SER MENOR QUE O SEGUNDO PARA DETERMINAR O INTERVALO!!!')
"""

"""
22 - Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de
notas (válidas no intervalo de 10 a 20) e que mostre na tela, como resulado, a correspondente média aritmédica. O
número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará quando for
introduzido um valor que não seja válido como nota de aprovação.

nota_apro = 16
nota_aluno = 0
qtd_nota = 0
notas = []

while nota_aluno < nota_apro:
    nota_aluno = float(input('Informe a nota do aluno: '))
    if nota_aluno >= 10 and nota_aluno <= 20:
        qtd_nota += 1
        lista_notas = notas.append(nota_aluno)
        lista_notas = sum(notas)
        media_notas = lista_notas / qtd_nota

    else:
        print('INFORME UMA NOTA DENTRO DE INTERVALO ESTABELECIDO ( 10 ATÉ 20)')
print(f'Foram infomadas {qtd_nota:.0f} notas sendo elas {notas} e a média aritmédica foi {media_notas}')
print('!!!!!FIM!!!!!')
"""

"""
23 - Faça um algoritmo que leia um número positivo e imprima seus divisores.

num = int(input('Informe o 1º número positivo: '))

lista_num = []

if num > 0:
    for n in range(1, num+1):
        div_num = num / n
        if div_num % 2 == 1 or div_num % 2 == 0:
            lista_n_num = lista_num.append(n)
    print(f'O número informado foi {num} e seus divisores são {lista_num}.')
else:
    print('!!!!!NECESSÁRIO INFORMAR UM NÚMERO POSITIVO!!!!')
"""

"""
24 - Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção
dele próprio. Ex. a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

num = int(input('Informe um número inteiro: '))

lista_num = []

if num > 0:
    for n in range(1, num):
        div_num = num / n
        if div_num % 2 == 1 or div_num % 2 == 0:
            lista_div = lista_num.append(n)
            soma_lista_div = sum(lista_num)
    print(f' O número informado foi {num} e a lista de divisores é = {lista_num} e a somada destes divisores é = '
          f'{soma_lista_div}.')

else:
    print('!!!O NÚMERO INFORMADO DEVE SER INTEIRO E POSITIVO!!!')
"""

"""
25 - Faça um programa que some todos os números naturais abaixo de 1000 que são multiplos de 3 e 5.

num3 = 3
num5 = 5
lista = []
for n in range(1, 1_000):
    num = n / num3
    num1 = n / num5
    if num % 2 == 1 and num1 % 2 == 1:
        lista1 = lista.append(n)
        lista1 = sum(lista)
print(f' Os números naturais abaixo de 1000 que são multiplos de 3 e 5 são: {lista}\n'
      f' e a soma deles é = {lista1}.')
"""

"""
26 - Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.


numero = int(input('Informe um número: '))

while True:
    numero += 1
    if numero % 11 == 0:
        print(f'O número {numero} é múltiplo de 11')
        break
    elif numero % 13 == 0:
        print(f' O número {numero} é multiplo de 13')
        break
    elif numero % 17 == 0:
        print(f' O número {numero} é multiplo de 17')
        break
"""

"""
27 - Em matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmónica:
            H(n) = 1 + 1/2 + 1/3 + 1/4 +...1/n
    Faça um programa que leia um valor n inteiro e positivo e apresente o valor H(n).

numerador = 1
numero = 0
denominador = 0
numero = int(input('Insira um número inteiro e positivo.'))
harmonica = 0
for n in range(1, numero + 1):
    if numero > 0:
        denominador = denominador + 1
        harmonica += (numerador/denominador)

        print(f'{numerador / denominador:.3f}', end=' + ')

print(f'\nA média harmônica é = {harmonica:.4f}')
"""

"""
28 - Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a formula:
E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!


import math

numero = int(input('Informe um número: '))
if numero > 0 :
    resultado = 1
    for numero in range (2, (numero+1)):
        fatorial = math.factorial(numero)
        resultado += 1 / fatorial
        print(f' O valor E = {resultado:.2f}')
else:
    print('O número informado não é positivo!!!')
"""

"""
29 - Escreva um programa para calcular o valor da série, para 5 termos.
S = 0 + 1/2! + 2/4! + 3/6! ... 

from math import factorial
f, numerador = 1, 0
n = 0
cont = 1
s = 0

while cont <= 5:
    n = n + 2 # denominador vai ser um numero par até 10
    f = factorial(n)
    numerador += 1
    s = (numerador / f) + s
    cont += 1
    print(f'{numerador}/{f} = {s:.2f}')
print(f'O valor final de S é: {s:.4f}')
"""

"""
30 - Faça programas para calcular as seguintes sequências:
1 + 2 + 3 + 4 + 5+ ... + n
1 - 2 + 3 - 4 + 5 +...+ (2n - 1)
1 + 3 + 5 + 7 +...+(2n - 1)
"""

"""
31 - Faça um programa que calcule e escreva o valor de S

S = 1/1 + 1/3 + 5/3 + 7/4...99/50

denominador = 0
resultado = 0

for n in range(1,101,2):
    denominador += 1
    divisao = n / denominador
    resultado += divisao

    print(f'{n} / {denominador}',)
print(f' A soma de todos os termos anteriores é igual a {resultado:.2f}')
"""

"""
32 - Faça um programa que simule o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número de cada dado
e relação entre eles (<,>,=) de cada lançamento.

import random
N = input('Os dados devem rolar? [S / N]\n').upper()
while N == 'S':
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 > d2:
        print(f'O primeiro dado deu {d1} e é maior do quê o segundo que deu {d2}')
        input('Os dados devem rolar novamente [S / N]\n').upper()

    elif d1 > d2:
        print(f'O primeiro dado deu {d1} e é maior do quê o segundo que deu {d2}')
        input('Os dados devem rolar novamente [S / N]\n').upper()

    elif d1 == d2:
        print(f'O primeiro dado deu {d1} e é maior do quê o segundo que deu {d2}')
        input('Os dados devem rolar novamente [S / N]\n').upper()
"""

"""
33 - Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros 
naturais que são multiplos de i e ou de ambos. Exemplo:
Para n = 6, i = 2 e j = 3 a saída deverá ser 0,2,3,4,6,8.

n = int(input('Informe o valor de n: '))
i = int(input('Informe o valor de i: '))
j = int(input('Informe o valor de j: '))

cont = 0
for g in range(0, n+100):
    if g % i == 0 or g % j == 0:
        cont += 1
        if cont <= n:
            print(g, end=',')
"""

"""
34 - Faça um programa que calcule o menor divisível por cada um dos números de 1 a 20? Ex: 2520 é o menor número que
pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""

"""
35 - Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. O usuário define o
valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números ímpares contidos
neste intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve ser
escrito uma mensagem de erro na tela, "Intervalo de valores inválido" e o programa termina. Exemplo de tela de saída:
Digite o valor inicial e o valor final: 5 10
Soma dos ímpares neste intervalo: 21

valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))

for n in range(0, 1):
    if valor_inicial > valor_final or valor_inicial < 0:
        print('Intervalo de valores inválido')
        break
    else:
        valor_int = []
        lista = []

        for n in range(valor_inicial, valor_final+1):
            if n % 2 == 1:
                lista = valor_int.append(n)
                lista = sum(valor_int)
    print(f' Os elementos {valor_int} correspondem aos elementos impares do valor inicial {valor_inicial} e o valor final'
          f'{valor_final} informados e a soma deles é = {lista}.')
"""

"""
36 - Faça um programa que calcule a diferença entre a soma dos quadrdos dos primeiros 100 números naturais e o quadrado
da soma. Ex:. A soma dos quadrados dos dez primeiros números naturais é 1² + 2² + 3² ... 10² = 385
O quadrado da soma dos dez primeiros números naturais é, (1 + 2 + 3 + .... + 10)² = 552 = 3025
A diferença entre a soma dos quadrdos dos dez primeiros números naturais é o quadrdo da soma é 3025 - 385 = 2640

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
quadrado_num = []
quadrado_sum = []

for n in range(n1,n2+1):
    num = n**2
    lista = quadrado_num.append(num)
    soma_lista = sum(quadrado_num)
    lista1 = quadrado_sum.append(n)
    soma_lista1 = sum(quadrado_sum)
    soma_lista1 = soma_lista1**2
    diferenca_quadrados = soma_lista1 - soma_lista
print(f' A soma dos quadrados dos primeiros números naturais de {n1} até {n2} é = {soma_lista} e o quadrado das soma'
      f'destes números é = {soma_lista1} e a diferênça entre eles é = {diferenca_quadrados}.')
"""

"""
37 - Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte:
A soma dos dois dígitos de mais alta ordem elevada ao quadrado é igual ao próprio número. Por exemplo, para o inteiro
3025, temos que:
30 + 25 = 55
55² = 3025

lista = []
for n in range(1000, 9999+1):
    num = str(n)
    prim_2 = int(num[0:2])
    ultm_2 = int(num[2:4])
    soma = (prim_2 + ultm_2)**2
    if soma == n:
        lista1 = lista.append(n)
print(lista,end=',')
"""
"""
38 - Faça um programa que calcule o terno pitagórico a,b,c, para o qual a+b+c = 1000. Um terno pitagórico é um conjunto
de três números naturais a,b,c para o qual, a² + b² = c² Por Exemplo: 3² + 4² = 9 + 16 = 25 = 5²

import math

a = int(input('Informe o valor do lado "A": '))
b = int(input('Informe o valor do labo "B": '))

lado_a = a**2
lado_b = b**2

c = lado_a + lado_b
lado_c = math.sqrt(c)
print(c)
print(lado_c)
# Interpretação propria deve estar errado.
# Resolução de colegas curso:

"""
"""
39 - Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário. Esse programa
não permitir a entada de dados inválidos, ou seja medidas menores ou iguais a 0.

base = int(input('Informe a medida da base do triângulo: '))
altura = int(input('Informe a medida da altura do triângulo: '))

if base > 0 and altura > 0:
    area = (base * altura) / 2
    print(f' As medidas refernte ao triângulo foi base = {base} e altura = {altura}; sendo assim a área deste triângulo'
          f'é = {area}m².')
"""
"""
40 - Faça um prgrama que faça leitura de vários números inteiros, até que se digite um número negativo. Esse programa 
tem que retornar o maior e o menor número lido.

num = 0
lista = []
while num > 0:
    num = int(input('Informe o número (Para o programa se for negativo: '))
    if num > 0:
        lista1 = lista.append(num)
        maior = max(lista)
        menor = min(lista)
print(f' Os números digitados exeto o negativo foi: {lista} o menor é: {menor} e o maior é: {maior}.')
"""

"""
41 - Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via
teclado. O programa fica pedindo estes valores e calculando até que o usuário entre com valor para resistência igual a 
zero. R = (R1 * R2) / (R1 + R2) 

r1 = 1
r2 = 1
lista = []

while r1 != 0 or r2 != 0:
    r1 = int(input('Informe o valor da resistência do resistor (R1) programa para quando valor é igual a zero: '))
    r2 = int(input('Informe o valor da resistência do resistor (R2) programa para quando valor é igual a zero: '))
    if r1 == 0 or r2 == 0:
        print(f' Valor informado foi R1 = {r1} e R2 = {r2}; sendo assim o programa foi parado!!!')
        break
    else:
        r = (r1 * r2) / (r1 + r2)
        print(f' Valor de r1 informado foi R1={r1} e R2={r2}; sendo assim o valor do paralelo das resistências é = '
              f'{r:.2f} Ohms.')
"""

"""
42 - Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos 
valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.


import math

num = 1
lista_num = []
lista_quadrado = []
lista_cubo = []
lista_raiz = []

while num > 0:
    num = int(input('Informe um número: '))
    if num <= 0:
        print(f' Programa foi finalizado pois o último número digitado foi {num} negativo ou zero')
        break
    lista1 = lista_num.append(num)
    num_quad = num**2
    num_cubo = num**3
    num_raiz = math.sqrt(num)
    lista1 = lista_quadrado.append(num_quad)
    lista1 = lista_cubo.append(num_cubo)
    lista1 = lista_raiz.append(f'{num_raiz:.2f}')

print(f' Os números digitados que atendem a regra dos cálculos foram: {lista_num} \n '
      f'elevado ao quadrado ficam = {lista_quadrado} \n'
      f' elevado ao cubo ficam = {lista_cubo} \n '
      f'tirando a raiz quadrada ficam = {lista_raiz}')
"""

"""
43 - Faça um programa que leia um número indeterminado de idade de indivíduos (pare quando for informado 
a idade 0 "Zero"), e calcule a idade média desse grupo.

idade = 1
cont = 0
lista = []

while idade > 0:
    idade = int(input('Informe a idade do individuo: '))
    if idade == 0:
        print(f'O programa foi finalizado pois a última idade digitada foi = {idade}'.upper())
        break
    cont += 1
    lista1 = lista.append(idade)
    lista1 = sum(lista)
    media = lista1 / cont
print(f'As idades informadas diferentes de zero foi: {lista}, totalizando {cont} idades digitadas e somando {lista1} '
      f'anos \nA média aritimetica das idades digitadas diferentes de zero resultou em : {media} anos')
"""

"""
44 - Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior 
ao número lido. Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34.

soma = 0
num_atual = 0
num_anterior = 1
sequencia = [0, 1]

numero = int(input('Digite um número para cálcular a sequência: '))

while numero < 0:
    print('Você deve digitar um número positivo!')
    numero = int(input('Digite um número para cálcular a sequência: '))
while True:
    soma = num_atual + num_anterior
    num_anterior = max(sequencia)
    sequencia.append(soma)
    if max(sequencia) > numero:
        break
    else:
        num_atual = soma
print(sequencia)
"""

"""
45 - Faça um algoritimo que converta uma velocidade empressa em km/h para m/s e vice versa. você deve criar um menu com 
as duas opções de conversão e com uma opção para finalizar o programa. O usuário poderá fazer quantas conversões desejar,
sendo que o programa só será finalizado quando a opção de finalizar for escolhida.


print('Informe a opção a ser executada?\n'
      'S = Sim\n'
      'N = Não')
opcao = input('Deseja executar uma conversão de velocidades? '.upper())
Sim = 'S'
sim = 's'

km = 0
ms = 0

while opcao == sim or opcao == Sim:

    km = input('Conversão km/h para m/s? (S / N): '.upper())
    if km == Sim or km == sim:
        km = int(input('Informe a velocidade em km/h: '))
        ms = 3.6
        ms = km / ms
        print(f' A velocidade informada em km/h foi:{km:.2f}km/h que corresponde a:{ms:.2f}m/s.')
    opcao = input('Deseja executar uma nova conversão de velocidades? '.upper())

    while opcao == sim or opcao == Sim:
        ms = input('Conversão m/s para km/h? (S / N): '.upper())

        if ms == Sim or ms == sim:
            ms = int(input('Informe a velocidade em m/s: '))
            km = 3.6
            kmh = ms * km
            print(print(f' A velocidade informada em m/s foi:{ms:.2f}m/s que corresponde a:{kmh:.2f}km/h.'))
        opcao = input('Deseja executar uma nova conversão de velocidades? '.upper())

print('O programa foi finalizado!!!')
"""

"""
46 - Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual o número foi gerado, 
cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. o programa acaba quando o
usuário acertar o número gerado. O programa deve informar em quantas tentativas o número foi descoberto

from random import randint
cont = 1

while cont > 0:
    cont += 1
    num = int(input('Faça seu palpite do número que será sorteado: '.upper()))
    sorteado = randint(1, 1000)

    if num > sorteado:
        print('O número informado é maior que o número sorteado')

    elif num < sorteado:
        print('O número informado é menor que o número sorteado')

    else:
        num == sorteado
        print(f'Voce acertou o número sorteado foi {sorteado} e você informou o número {num}'.upper())
        print('!!!! Programa Finalizado !!!'.upper())
        break
"""

"""
47 - Faça um rpograma que apresente um menu de opções para o cálculo das seguintes operações entre dois números:

adição (opção 1)
subtração (opção 2)
multiplicação (opção 3)
divisão (opção 4)
saída (opção 5)

O programa deve possibilidade ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de
opções. O programa só termina quando for escolhida a opção de saída (opção 5) 

print ('opções de operações: \n'.upper())
print ('1 = Adição\n'
       '2 = Subtração'
       '3 = Multiplicação\n'
       '4 = Divisão\n'
       '5 = Sair do Programa')
cont = 1

while cont > 0:
    cont += 1
    opcao = int(input('Informe a operação desejada: '.upper()))
    if opcao == 5:
        print('Você escolheu a opçao sair do programa\n'
              '!!!!!!  O programa foi finalizado  !!!!!!!!!!'.upper())
        break
    elif opcao == 1:
        print('Você escolheu a opçao adição: ')
        num = int(input('Informe o 1º número a ser somado: '))
        num1 = int(input('Informe o 2º número a ser somado: '))
        soma = num + num1
        print(f'Você digitou o número {num} e {num1} a soma dos números é = {soma}')

    elif opcao == 2:
        print('Você escolheu a opçao subtração: ')
        num = int(input('Informe o 1º número: '))
        num1 = int(input('Informe o 2º número: '))
        if num > num1:
            sub = num - num1
            print(f'Você digitou o número {num} e {num1} a subtração dos números é = {sub}')

        else:
            sub = num1 - num
            print(f'Você digitou como 1º número o {num} e o 2º foi {num1} a subtração do maior {num1} pelo menor'
                  f'{num} é = {sub}')

    elif opcao == 3:
        print('Você escolheu a opçao multiplicação: ')
        num = int(input('Informe o 1º número: '))
        num1 = int(input('Informe o 2º número: '))
        mult = num * num1
        print(f'Você digitou o número {num} e {num1} a multiplicação dos números é = {mult}')

    elif opcao == 4:
        print('Você escolheu a opçao divisão: ')
        num = int(input('Informe o 1º número: '))
        num1 = int(input('Informe o 2º número: '))

        if num > num1:
            div = num / num1
            print(f'Você digitou o número {num} e {num1} a divisão  de {num} por {num1} é = {div:.0f}')

        else:
            div = num1 / num
            print(f'Você digitou como 1º número o {num} e o 2º foi {num1} a divisão do maior {num1} pelo menor'
                  f' {num} é = {div:.0f}')
"""

"""
48 - Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos valores não ultrapassem quadro
milhões.
"""

"""
49 - O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu
salário. Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois
está rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês.
Construa um programa que deverá calcular e mostrar a quantidade de meses necessário que o valor pertecente a João
iguale ou ultrapasse o valor pertecente a Carlos. Teste com outros valores para as taxas.

salario_carlos = int(input('Informe o salário de Carlos a ser investido na poupança: '))
salario_carlos_in = salario_carlos

salario_joao = salario_carlos / 3
salario_joao_in = salario_joao

poupanca = 0.02
renda_fixa = 0.05
cont = 0

while salario_joao <= salario_carlos:
    cont += 1
    salario_carlos = salario_carlos + (salario_carlos * poupanca)
    salario_joao = salario_joao + (salario_joao * renda_fixa)
    if salario_joao >= salario_carlos:
        break

print(f'Inicialmente Carlos aplicou R$ {salario_carlos_in:.2f} e João aplicou R$ {salario_joao_in:.2f} após {cont} meses '
      f'João terá R$ {salario_joao:.2f} e Carlos terá R$ {salario_carlos:.2f}.')
"""

"""
50 - Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centimentros para ano.
Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que chico.


chico = 1.50
chico_in = chico

ze = 1.10
ze_in = ze

cresc_chico = 0.02
cresc_ze = 0.05
cont = 0

while cont >= 0:
    cont += 1
    chico = chico + cresc_chico
    ze = ze + cresc_ze

    if ze >= chico:
        break

print(f'Inicialmente Chico tinha altuma de {chico_in:.2f}mts e o Zé tinha {ze_in:.2f}mts após {cont} anos Zé terá '
      f'{ze:.2f}mts e Chico terá {chico:.2f}mts.   ')
"""
"""
51 - Um funcionário recebe aumento anual. Em 1995 foi contratado por 2_000 reais. Em 1996 recebeu aumento de 1.5%.
Apartir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça programa que determine o salário atual
do funcionário.

salario_in = 2_000
ano_in = 1995
ano_atual = int(input('Informe o ano atual: '))
taxa_aumento = 0.015
salario = 0
ano = 0
cont = 0
cont1 = ano_atual - ano_in
if ano_atual >= ano_in:

    while ano_in <= ano_atual:
        cont += 1
        ano = ano_in + 1

        if cont <= 1:
            salario = salario_in + (salario_in * taxa_aumento)

        elif cont >= 2 and cont <= cont1:
            taxa_aumento = taxa_aumento * 2
            salario = salario + (salario * taxa_aumento)

        else:
            cont > cont1
            break
    print(
        f'salario de inicio foi de R$ {salario_in:.2f} no ano de {ano} ano incio {ano_in} - ano atua {ano_atual} = {cont1} '
        f'anos, obteve uma taxa de aumento acumulada em {taxa_aumento:.2f}% chegando ao salario de R$ {salario:.2f}')
else:
    print('Dados invalidos favor revisar!!!'.upper())
"""

"""
52 - Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas
notas de cada valor são necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas
notas de 100, 50, 20, 10, 5, 2 e 1 real.

from math import floor

saque = int(input('Informe o valor do saque: '))
saque_in = saque

qtd_nota100 = 0
qtd_nota50 = 0
qtd_nota20 = 0
qtd_nota10 = 0
qtd_nota5 = 0
qtd_nota2 = 0
qtd_nota1 = 0

nota100 = 100
nota50 = 50
nota20 = 20
nota10 = 10
nota5 = 5
nota2 = 2
nota1 = 1

while saque >= 100:
    qtd_nota100 = saque / nota100

    if qtd_nota100 >= 1:
        qtd_nota100 = floor(qtd_nota100)
        saque = saque - (nota100 * qtd_nota100)


while saque >= 50:
    qtd_nota50 = saque / nota50

    if qtd_nota50 >= 1:
        qtd_nota50 = floor(qtd_nota50)
        saque = saque - (nota50 * qtd_nota50)

while saque >= 20:
    qtd_nota20 = saque / nota20

    if qtd_nota20 >= 1:
        qtd_nota20 = floor(qtd_nota20)
        saque = saque - (nota20 * qtd_nota20)

while saque >= 10:
    qtd_nota10 = saque / nota10

    if qtd_nota10 >= 1:
        qtd_nota10 = floor(qtd_nota10)
        saque = saque - (nota10 * qtd_nota10)

while saque >= 5:
    qtd_nota5 = saque / nota5

    if qtd_nota5 >= 1:
        qtd_nota5 = floor(qtd_nota5)
        saque = saque - (nota5 * qtd_nota5)

while saque >= 2:
    qtd_nota2 = saque / nota2

    if qtd_nota2 >= 1:
        qtd_nota2 = floor(qtd_nota2)
        saque = saque - (nota2 * qtd_nota2)

while saque >= 1:
    qtd_nota1 = saque / nota1

    if qtd_nota1 >= 1:
        qtd_nota1 = floor(qtd_nota1)
        saque = saque - (nota1 * qtd_nota1)

print(f'O valor de saque foi R$ {saque_in} seram fornecidas as seguintes notas:\n'
      f'Notas 100 = {qtd_nota100}\n'
      f'Notas 50 = {qtd_nota50}\n'
      f'Notas 20 = {qtd_nota20}\n'
      f'Notas 10 = {qtd_nota10}\n'
      f'Notas 5 = {qtd_nota5}\n'
      f'Notas 2 = {qtd_nota2}\n'
      f'Notas 1 = {qtd_nota1}\n'
      f'Restando {saque:.2f} de diferença do saque')
"""

"""
53 - Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado triangulo de 
Floyd. para n = 6 termos:

1
2 3
4 5 6
7 8 9 10
11 12 13 14
15 16 17 18 19

n = int(input('Digite um número inteiro positivo: '))
soma = 0

for i in range(1, n + 1):
    soma += i
    for num in range (soma - i + 1, soma + 1):
        print(num, end=' ')
    print()
"""

"""
54 - Faça um programa que leia um número inteiro maior que 1, e verifique se o número fornecido é primo ou não.
"""
"""
55 - Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros números primos.
"""

"""
56 - Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões.
"""

"""
57 - Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números informados pelo 
usuário.
"""

"""
58 - Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados pelo usuário.
"""

"""
59 - Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kwh, e para cada 
habiltante entre com os seguintes dados: consumo do mês e o código do consumidor (1- Residencial, 2 Comercial,
3- Industrial). No final imprima o maior, o menor e a média do consumo dos habitantes; e por fim o total do consumo de
cada categoria de consumidor.

num_hab = int(input('Informe o número de habitantes da cidade: '))
kwh_cid = .36
cont = 0
lista1 = []
lista2 = []
lista3 = []
lista_geral = []

while cont <= (num_hab - 1):
    cont += 1
    print('CÓDIGOS DE HABILTANTES:\n'
          '1 = Residencial\n'
          '2 = Comercial\n'
          '3 = Industrial')
    cod_hab = int(input(f'Informe o código do habiltante {cont}: '))
    cons_hab = int(input(f'Informe o consumo do mês para o habilante {cont}: '))

    if cod_hab == 1:
        lista = lista1.append(cons_hab)
        lista = lista_geral.append(cons_hab)

    elif cons_hab == 2:
        lista4 = lista2.append(cons_hab)
        lista5 = lista_geral.append(cons_hab)

    elif cod_hab == 3:
        lista6 = lista3.append(cons_hab)
        lista7 = lista_geral.append(cons_hab)

    elif cod_hab < 1 or cod_hab > 3:
        print('!!!!Código do consumidor inexistente !!!!!!'.upper())
        # lista_geral.pop()
        cont -= 1


maior = max(lista_geral)
menor = min(lista_geral)
media = sum(lista_geral) / num_hab

soma_res = sum(lista1)
soma_com = sum(lista2)
soma_ind = sum(lista3)

print(f'Consumo Residencial = {lista1}kwh\nConsumidores Comercial = {lista2}kwh\nConsumidores Industrial = {lista3}kwh\n'
      f'Soma Residêncial = {soma_res}kwh\nSoma Comercial = {soma_com}kwh\nSoma Industrial = {soma_ind}kwh\n'
      f'Consumo Geral = {lista_geral}kwh\nMaior Geral = {maior}kwh\nMenor Geral = {menor}kwh\nMédia Geral = {media}kwh')
"""

"""
60 - Faça um programa que leia vários números, calcule e mostre:
a - A soma dos números digitados
b - A quantidade de números digitados
c - A média dos números digitados
d - O maior número digitado
e - O menor número digitado
f - A média dos números pares

Finalize a entrada de dados caso o usuário informe o valor 0.

cont = 0
cont1 = 0
lista_geral = []
soma = 0
qtd_num = 0
media = 0
maior = 0
menor = 0

media_par = 0
lista_par = []

while cont >= 0:

    num = int(input('Digite um número à ser considerado nos cálculos ou zero para Sair: '))
    if num != 0:
        cont += 1
        lista = lista_geral.append(num)
        soma = sum(lista_geral)
        qtd_num = cont
        media = soma / qtd_num
        maior = max(lista_geral)
        menor = min(lista_geral)
        if num % 2 == 0:
            cont1 += 1
            media_pares = lista_par.append(num)
            soma_par = sum(lista_par)
            qtd_par = cont1
            media_par = soma_par / qtd_par

    else:
        print('Você digitou zero = Sair do Programa'.upper())
        break

print(f'A soma dos números digitados = {soma}\n'
      f'A quantidade de números digitados = {qtd_num}\n'
      f'A média dos números digitados = {media}\n'
      f'O maior número digitado = {maior}\n'
      f'O menor número digitado = {menor}\n'
      f'A média dos números pares = {media_par}')
"""

"""
61 - Faça um programa que calcule o maior número palidromo feito a partir do produto de dois números de 3 dígitos.
Ex.: O maior palindromo feito apartir do produto de dois números de dois digitos é 9009 = 91*99
"""

"""
62 - Se os números de 1 a 5 são escritos em palavras: um dois, três, quadro, cinco, então há 2 + 4 + 4 + 5 = 22 letras
usadas no total. Faça um programa que conte quantas letras seriam utilizadas se tod os números de 1 a 1000 fossem 
escritos em palavras.
Obs. Não conte espaços ou hifens.
"""






