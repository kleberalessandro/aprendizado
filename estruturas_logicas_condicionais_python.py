"""
1 - Faça um programa que receba dois números e mostre qual deles é o maior.

num1 = float(input('Qual primeiro número? '))
num2 = float(input('Qual o segundo número? '))

if num1 > num2:
    print('O primeiro número é maior que o segundo número')
else:
    print('O segundo número é maior que o primeiro número')
"""

"""
2 - Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número
for negativo, mostre um a mensagem dizendo que o número é inválido.


import math

num = int(input('Informe um número? '))

if num > 0:
    print(f'A raíz quadrada de {num} é {math.sqrt(num):.0f}')

else:
    print('Número inválido!!')
"""

"""
3 - Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário imprima o número ao quadrado.

import math

num = float(input("Informe o número "))
num2 = num**2
if num > 0:
    print(f'A raiz quadrada do número é {math.sqrt(num):.0f}')
else:
    print(f'O quadrado do número é {num2:.0f}')
"""

"""
4 - Faça um programa que leia um número e, caso ele seja positivo, clacule e mostre:
        -   O número digitado ao quadrado
        -   A raiz quadrada do número digitado

import math
num = float(input('Informe o número: '))

if num > 0:
    print(f'O número digitado ao quadrado é = {num**2:.2f}\n'
          f'A raiz quadada do número é = {math.sqrt(num):.2f}')
"""

"""
5 - Faça um programa que receba um número inteiro e verifique se este número é par ou impar.

num = float(input('Informe um número: '))
if num % 2 == 0:
    print(f'O número informado foi o número {num:.0f} e é par')
else:
    print(f'O número informado fo o número {num:.0f} e é impar')
"""

"""
6 - Esceva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente 
entre ambos.

num1 = int(input('Informe o primeiro número inteiro: '))
num2 = int(input('informe o segundo número inteiro: '))
num1_maior = num1 - num2
num2_maior = num2 - num1

if num1 > num2:
    print(f'O primeiro número: {num1:.0f} é maior que o segundo número {num2:.0f} e suas diferenças é ='
          f'{num1_maior:.0f}')
else:
    print(f'O segundo número : {num2:.0f} é maior que o primeiro número {num1:.0f} e suas diferenças é = '
          f'{num2_maior:.0f}')
"""

"""
7 - Faça um programa que receba dois números e mostre o maior. por acaso ou dois números forem iguais, imprima a 
mensagem números iguais.

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

if num1 > num2:
    print(f'O primeiro número {num1:.0f} e é maior que o segundo número {num2:.0f}; informados')
if num2 > num1:
    print(f'O segundo número {num2:.0f} e é maior que o primeiro número {num1:.0f}; informados')
elif num1 == num2:
    print(f'O primeiro número "{num1:.0f}" é igual ao segundo número "{num2:.0f}"; informados')
"""

"""
8 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas 
notas. Uma nota válida deve ser, obrigatóriamente, um valor entre 0.0 e 10.0, onde caso a não possua um valor válido,
este fato deve ser informado ao usuário e o programa termina.
"""

"""
9 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do 
salário imprima: Emprestimo não concedido, caso contrário imprima: Empréstimo concedido.

salario = float(input('Infome o salario R$ '))
valor_prestaçao = float(input('Informe o valor da prestação R$ '))
perc_sal_prest = valor_prestaçao / salario
if perc_sal_prest > 0.20:
    print('Emprestimo não concedido')
else:
    print(('Emprestimo Concedido'))
"""

"""
10 - Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as
seguintes fórmulas (onde h corresponde a altura):   Homens = (72.7 * h) - 58
                                                    Mulheres = (62,1 * h) - 44,7
altura = float(input('Qual a altura da pessoa? '))
sexo = int(input('Qual o sexo da pessoa? Masculino = 1 e Feminina = 2 '))
fem = (altura * 72.7) - 58
mas = (altura * 62.1) - 44.7
print(mas)
print(fem)
print(sexo)
if sexo == int(1):
    print(f'{mas:.2f}')
if sexo == int(2):
    print(f'{fem:.0f}')
else:
    print('Verificar; pois os dados informados estão incorretos!!')
"""

"""
11 - Escreva um programa que leia um número inteiro maior que zero e devolva, na tela, a soma de todos os seus 
algarismos. Por exemplo, ao 251 corresponderá o valor 8 ( 2 + 5 + 1). Se o número não for maior que zero o programa 
terminará com a mensagem " Número invpalido".


n1 = int(input('Informe o número: '))
s = 0

for n in n1:
    s = s + int(n)

print(f' A soma dos algarismos de {n1} é {s}')

# resolução de forma matemática: 
num = int(input('Informe o número: '))
m = num // 1 % 10
c = num // 10 % 10
d = num // 100 % 10
u = num // 1000 % 10
soma = u + d + c + m
print(f'O numero {soma} é a soma dos digitos {u} - {d} - {c} - {m} que corresponde ao número digítado foi : {num}')
"""

"""
12 - Ler um número inteiro. Se o número for negativo, escreva a mensagem "Número invalido". Se o número for positivo,
calcular o logaritimo deste número.

import math

n = int(input('Informe um número inteiro: '))
a = 10
x = ()

if n <= 0:
    print('Número invalido')
else:
    print(math.log10(n))
"""

"""
13 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e segunda prova têm peso 1 e a
terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado. A nota para aprovação de ser
igual ou superior a 60 pontos.

nota1 = float(input('Informa a nota 1: '))
nota2 = float(input('Informar a nota 2: '))
nota3 = float(input('Informar a nota 3: '))
peso_nota1 = 1
peso_nota2 = 1
peso_nota3 = 2

nota1_pond = nota1 * peso_nota1
nota2_pond = nota2 * peso_nota2
nota3_pond = nota3 * peso_nota3

media_pond  = (nota1_pond + nota2_pond + nota3_pond) / (peso_nota1 + peso_nota2 + peso_nota3)

if media_pond == 60:
    print(f'Aluno aprovado!! média da nota {media_pond} igual a 60 pontos')
elif media_pond > 60:
    print(f'Aluno aprovado!! média da nota {media_pond} maior que 60 pontos')
else:
    print(f'Aluno reprovado!! Média = {media_pond} menor que 60 pontos')
"""

"""
14 - A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 a 10,
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um final. A média das três notas 
mencionadas anteriormente obedece aos pesos: Trabalho de labortório: 2; Avaliação Semenstral: 3; Exame Final: 5. 
De acordo com o resultado, mostre na tabela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 
4,9) ou foi aprovado. Faça todas as verificações necessárias. 

nota_lab = float(input('Informe a nota de 0 a 10 do trabalho de laboratório: '))
nota_ava = float(input('Informe a nota de 0 a 10 da avaliação semestral: '))
nota_exa = float(input('Informe a nota de 0 a 10 do exame final: '))

peso_lab = 2
peso_ava = 3
peso_exa = 5

media = ((nota_lab*peso_lab) + (nota_ava*peso_ava) + (nota_exa*peso_exa) ) / (peso_lab + peso_ava + peso_exa)

if media >= 0 and media < 2.9:
    print(f'Aluno reprovado a média da nota foi {media:.2f}')
elif media >= 2.9 and media <= 4.9:
    print(f'Aluno em recuperação a média da nota é {media:.2f}')
elif media > 4.9 and media <= 10:
    print(f'Aluno aprovado a média da nota foi {media:.2f}')
else:
    print(f'As notas {nota_lab} ou {nota_exa} ou {nota_ava} - informadas são invalidas')
"""

"""
15 - Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este
numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

dia = int(input('Informe um dia entre 1 e 7:'))
while dia < 1 or dia > 7:
    dia == int(input('Informe um dia entre 1 e 7!! '))
if dia == 1:
    print(f'Hoje é dia {dia}, Domingo')
elif dia == 2:
    print(f'Hoje é dia {dia}, Segunda-feira')
elif dia == 3:
    print(f'Hoje é dia {dia}, Terça-feira')
elif dia == 4:
    print(f'Hoje é dia {dia}, Quarta-feira')
elif dia == 5:
    print(f'Hoje é dia {dia}, Quinta-feira')
elif dia == 6:
    print(f'Hoje é dia {dia}, Sexta-feira')
elif dia == 7:
    print(f'Hoje é dia {dia}, Sábado')
"""

"""
16 - Usando switch, escreva um programa, que leia um número entre 1 e 12 e imprima o mês correspondente a este número.
Isto é, janeiro se 1, fevereiro se 2, e assim por diante.

mes = int(input('Informe um número entre 1 e 12: '))
while mes < 1 and mes > 12:
    mes == int(input('Informe um número entre 1 e 12!!'))
if mes == 1:
    print(f'O número {mes}, corresponde ao mês de Janeiro')
elif mes == 2:
    print(f'O número {mes}, corresponde ao mês de Fevereiro')
elif mes == 3:
    print(f'O número {mes}, corresponde ao mês de Março')
elif mes == 4:
    print(f'O número {mes}, corresponde ao mês de Abril')
elif mes == 5:
    print(f'O número {mes}, corresponde ao mês de Maio')
elif mes == 6:
    print(f'O número {mes}, corresponde ao mês de Junho')
elif mes == 7:
    print(f'O número {mes}, corresponde ao mês de Julho')
elif mes == 1:
    print(f'O número {mes}, corresponde ao mês de Agosto')
elif mes == 1:
    print(f'O número {mes}, corresponde ao mês de Setembro')
elif mes == 10:
    print(f'O número {mes}, corresponde ao mês de Outubro')
elif mes == 11:
    print(f'O número {mes}, corresponde ao mês de Novembro')
elif mes == 12:
    print(f'O número {mes}, corresponde ao mês de Dezembro')
"""

"""
17 - Faça um programa que clacule e mostre a área de um trapézio. Sabe-se que: A = (Base Maior + Base Menor) / 2
Lembre-se a base maior e a base menor devem ser maiores que zero. 

base_maior = float(input('Informe a medida da base maior: '))
base_menor = float(input('Informe a medida da base menor: '))
area = (base_menor + base_maior) / 2

while base_menor <= 0 or base_maior <= 0:
    area == input('A medida da bases maior e da base menor devem ser maior que zero!!!')

if area > 0:
    print(f'A área do trapézio é = {area}m²')
"""

"""
18 - Faça um programa que mostre ao usuário um menu com 4 opções matemáticas (as básicas, por exemplo). O usuário 
escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado
e saindo.

opcoes = float(input('Sendo:\n 1 = Adição\n 2 = Subtração\n 3 = Divisão\n 4 = Multiplicação\n'
                     'Informe a opção matemática: '))

while opcoes < 1 or opcoes > 4:
    print('Infome um número de 1 até 4 correspondente a operação matemática desejada!!')
    opcoes = float(input('Sendo:\n 1 = Adição\n 2 = Subtração\n 3 = Divisão\n 4 = Multiplicação\n'
                         'Informe a opção matemática: '))

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))

if opcoes == 1:
    operacao = n1 + n2
    print(f'A operação selecionada foi 1 (Adição) e o resultado de {n1} + {n2} = {operacao}')
elif opcoes == 2:
    operacao = n1 - n2
    print(f'A operação selecionada foi 2 (Subtração) e o resultado de {n1} - {n2} = {operacao}')
elif opcoes == 3:
    operacao = n1 / n2
    print(f'A operação selecionada foi 3 (Divisão) e o resultado de {n1} / {n2} = {operacao}')
elif opcoes == 4:
    operacao = n1 * n2
    print(f'A operação selecionada foi 4 (Multiplicação) e o resultado de {n1:.0f} * {n2:.0f} = {operacao}')
else:
    print('Infome um número de 1 até 4 correspondente a operação matemática desejada!!')
"""

"""
19 - Faça um programa para verificar se um determinado número é divisível por 3 ou 5, mas não simultanemente pelos dois.

num = float(input('Informe um número: '))
div3 = num % 3
div5 = num % 5

if div3 == 0 or div5 == 0:
    print('Número é divisível por 3 ou 5')
else:
    print('O número informado não é divisível por 3 ou por 5')
"""

"""
20 - Dados três valores A, B, C verifique se os valores podem ser dos lados de um triângulo e se for se são de um 
triâgulo escaleno, equilatero ou isoceles, considerando os seguintes conceitos:

O comprimento de cada lado de um triângulo é menor que a soma dos dois lados

Isoceles são triângulos que tem os três lados iguais
Equilatero denomina-se triângulos que tem o comprimento com dois lados iguais
Recebe o  nome de triângulo isoceles o que têm os três lados diferentes 

a = float(input('Informe o valor de A: '))
b = float(input('informe o valor de B: '))
c = float(input('Informe o valor de c: '))

if a < b + c or b < a + c or c < b + a:
    if a == b and a == c and b == c:
        print(f'O triângulo tem os três lados iguais sendo a = {a}; b = {b} e c = {c} assim é um equilatero!')
    elif a == b != c or a != b == b or a == c != b:
        print(f'O triângulo tem dois lados iguais sendo a = {a}; b = {b} e c = {c} assim é um isóceles!')
    elif a != b != c:
        print(f'O triângulo tem os três lados diferentes sendo a = {a}; b = {b} e c = {c} assim é um escaleno!')
else:
    print('Valores informados não correspondem a um triângulo')
"""

"""
21 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de
erro se a opção for inválida.

Escolha a opção:
1 - Soma de 2 números.
2 - Diferença entre 2 números (maior pelo menor).
3 - Produto entre 2 números.
4 - Divisão entre 2 números (o denominador não pode ser zero).


opcao1 = 1
opcao2 = 2
opcao3 = 3
opcao4 = 4
a = float(input('Escolha a opção: \n'
                '1 - Soma de 2 números \n'
                '2 - Diferença entre 2 números (maior pelo menor) \n'
                '3 - Produto entre 2 números \n'
                '4 - Divisão entre 2 números (o denominador não pode ser zero) '))

if a == opcao1:
    nun1 = float(input('Informe o primeiro número: '))
    nun2 = float(input('Informe o segundo número: '))
    soma = nun1 + nun2
    print(f'A soma dos 2 números informados é:{soma}')
if a == opcao2:
    nun1 = float(input('Informe o primeiro número: '))
    nun2 = float(input('Informe o segundo número: '))
    if nun1 > nun2:
        sub1 = nun1 - nun2
        print(f'O primeiro número é:{nun1} e o segundo é:{nun2} assim a subtração do primeiro pelo segundo é:{sub1}')
    if nun2 > nun1:
        sub2 = nun2 - nun1
        print(f'O segundo número é:{nun2} e o primeiro é:{nun1} assim a subtração do segundo pelo primeiro é:{sub2}')
    if nun1 == nun2:
        print('Os números informados são iguais portanto está fora da regra da opção escolhida.')

if a == opcao3:
    nun1 = float(input('Informe o primeiro número: '))
    nun2 = float(input('Informe o segundo número: '))
    produto = nun1 * nun2
    print(f'O produto entre o primeiro núnero:{nun1} e o segundo número:{nun2}; infofrmados é = {produto}')

if a == opcao4:
    nun1 = float(input('Informe o primeiro número (Deve ser diferente de zero): '))
    nun2 = float(input('Informe o segundo número (Deve ser diferente de zero): '))
    if nun1 and nun2 != 0 and nun1 > nun2:
        div = nun1 / nun2
        print(f'A divisão do primeiro número({nun1}) pelo segundo número({nun2}) informado é = {div}')

    if nun1 and nun2 != 0 and nun2 > nun1:
        div = nun2 / nun1
        print(f'A divisão do segundo número({nun2}) pelo primeiro número({nun1}) informado é = {div}')

    if nun1 and nun2 != 0 and nun2 == nun1:
        print('Os números infomados são iguais sendo assim está fora da regra estabelecida pois sua divisão será = zero')
"""

"""
22 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condicções para
aposentadoria são:
 - Ter pelo menos 65 anos;
 - Ou ter trabalhado pelo menos 30 anos;
 - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos. 

idade = float(input('Qual a idade do trabalhador? '))
tempo = float(input('Quanto tempo de trabalho? '))

if tempo > 65 or tempo >= 30 or idade >= 60 and tempo >= 25:
    print(f'O trabalhador tem {idade} e {tempo} de tempo de serviço; sendo assim já pode se aposentar')
else:
    print(f'O trabalhador tem {idade} e {tempo} de tempo de serviço e sendo assim: Ainda não pode se aposentar')
"""

"""
23 - Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for
divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996.

ano = float(input('Informe o ano? '))

if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano informado {ano:.0f} é bissexto')
else:
    print(f'O ano informado {ano:.0f} não é bissexto')
"""

"""
24 - Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imporsto
sobre o produto (MG 7%; SP 12%; RJ 15% e MS 8%). Faça um programa em que o usuário entre com o valor e o destino do
produto e o retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado 
digitado não for válido, mostrar uma mensagem de erro.

produto = float(input('Qual o valor do produto R$'))
estado = float(input('Indique qual estado de destino do produto:\n'
                     '1 = Minas Gerais \n'
                     '2 = São Paulo \n'
                     '3 = Rio de Janeiro \n'
                     '4 = Mato Grosso do Sul'))
mg = produto + (produto * 0.07)
sp = produto + (produto * 0.12)
rj = produto + (produto * 0.15)
ms = produto + (produto * 0.08)

if estado == 1:
    print(f'O produto tem destino para MG e o valor de R$ {produto:.0f},00 com imposto o valor passa a ser de '
          f'R$ {mg:.0f},00')
elif estado == 2:
    print(f'O produto tem destino para SP e o valor de R$ {produto:.0f},00 com imposto o valor passa a ser de '
          f'R$ {sp:.0f},00')
elif estado == 3:
    print(f'O produto tem destino para RJ e o valor de R$ {produto:.0f},00 com imposto o valor passa a ser de '
          f'R$ {rj:.0f},00')
elif estado == 4:
    print(f'O produto tem destino para MS e o valor de R$ {produto:.0f},00 com imposto o valor passa a ser de '
          f'R$ {ms:.0f},00')
else:

    print('Verifique estado selecionado pois não corresponde as opções disponíveis!!')
"""

"""
25 - Calcule as raízes da equação de 2º grau. Lembrando que: x = -b +- raiz delta / 2a onde B² - 4ac E ax² + bx + c = 0
representa uma equação de 2º grau.

A variável a tem que ser diferente de zero. Caso seja igual. imprima a mensagem "Não é equação de segundo grau"

 - Se Delta < 0, não existe real. Imprima a mensagem Não existe raiz
 - Se Delta = 0, existe uma raiz real. imprima a raiz e a mensagem Raiz única
 - Se >= 0, imprima as duas raízes reais
"""

"""
26 - Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o 
consumo em Km/l e escreva uma mensagem de acordo com a lista abaixo:

Consuno    (Km/l)    Mensagem
Menor que    8       Venda o carro!
Entre      8 e 14    Econômico!
Maior que    12      Super econômico!

distancia = float(input('Informe a distância percorrida em Km: '))
litros = float(input('Informe a quantidade de litros consumidos de gasolina: '))
consumo = distancia / litros
print(consumo)

if consumo < 8:
    print('Consuno    (Km/l)    Mensagem\n '
          'Menor que    8       Venda o carro!')

if consumo >= 8 and consumo <= 14:
    print('Consuno    (Km/l)    Mensagem\n '
          'Entre      8 e 14    Econômico!')

if consumo > 12:
    print('Consuno    (Km/l)    Mensagem\n '
          'Maior que    12      Super econômico!')
"""

"""
27 - Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:

Categoria       Idade
Infantil A      5 a 7
Infantil B      8 a 10
Juvenil A       11 a 13
Juvenil B       14 a 17
Sênior          maiores de 18 anos

idade = float(input('Qual a idade do nadador? '))

if idade >= 5 and idade <=7:
    print(f'O nadador tem {idade:.0f} anos de idade e é classificado conforme tabela abaixo:\n'
          f'Categoria       Idade \n'
          f'Infantil A      5 a 7')

if idade >= 8 and idade <=10:
    print(f'O nadador tem {idade:.0f} anos de idade e é classificado conforme tabela abaixo:\n'
          f'Categoria       Idade \n'
          f'Infantil B      8 a 10')

if idade >= 11 and idade <=13:
    print(f'O nadador tem {idade:.0f} anos de idade e é classificado conforme tabela abaixo:\n'
          f'Categoria       Idade \n'
          f'Juvenil A       11 a 13')

if idade >= 14 and idade <=17:
    print(f'O nadador tem {idade:.0f} anos de idade e é classificado conforme tabela abaixo:\n'
          f'Categoria       Idade \n'
          f'Juvenil B       14 a 17')

if idade >= 18:
    print(f'O nadador tem {idade:.0f} anos de idade e é classificado conforme tabela abaixo:\n'
          f'Categoria       Idade \n'
          f'Sênior          maiores de 18 anos')

else:
    print('Idade informada não corresponde aos intervalos relacionados')
"""

"""
28 - Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo
com um valor numérico digitado pelo usuário:
A - Geométrica: Raiz cubica (x * y * z)
B - Ponderada: (x + 2y + 3) / 6
C - Harmônica: ( 1 ) / ( (1/x) + (1/y) + (1/z) )
D - Arimética: ( x + y + z ) / 3

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

if num1 > 0 and num2 > 0 and num3 > 0:
    medias = int(input('1 = Geométrica\n'
                       '2 = Ponderada\n'
                       '3 = Harmônica\n'
                       '4 = Arimética\n'
                       'Informe o número correspondênte a média à ser cálculada:'))
    if medias == 1:
        geo = (num1 * num2 * num3) ** (1 / 3)
        print(f' A média Geométrica dos numérios {num1}, {num2} e {num3} infomados é = {geo:.0f}')

    if medias == 2:
        pon = ((num1 + (2 * num2)) + 3) / 6
        print(f' A média Ponderada dos numérios {num1} e {num2} infomados é = {pon:.0f}')

    if medias == 3:
        har = 1 / ((1/num1) + (1/num2) + (1/num3))
        print(f' A média Ponderada dos numérios {num1}, {num2} e {num3} infomados é = {har:.0f}')

    if medias == 4:
        ari = (num1 + num2 + num3) / 3
        print(f' A média Ponderada dos numérios {num1}, {num2} e {num3} infomados é = {ari:.0f}')

else:
    print(f'Número {num1} ou {num2} ou {num3} informado não atende a regra estabelecida; Inteiros e acima de zero')
"""

"""
29 - Faça um prova de matemática para crianças que estão aprendendo a somar números inteiros menores que 100.
Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: Qual é a soma de a + b, onde a e b são os 
números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.

from random import choice
a = choice(range(1, 100))
b = choice(range(1, 100))
c = a + b
resp = int(input(f'Qual é a soma de {a} + {b} = '))
if resp == (a + b):
    acerto = 1
    erro = 0
    print('Parabens Você acertou')
else:
    erro = 1
    acerto = 0
    print(f'Você errou a resposta {erro}')

a1 = choice(range(1, 100))
b1 = choice(range(1, 100))
c1 = a1 + b1
resp1 = int(input(f'Qual é a soma de {a1} + {b1} = '))
if resp1 == (a1 + b1):
    acerto1 = 1
    erro1 = 0
    print('Parabens Você acertou')
else:
    erro1 = 1
    acerto1 = 0
    print(f'Você errou a resposta {erro1}')

a2 = choice(range(1, 100))
b2 = choice(range(1, 100))
c2 = a2 + b2
resp2 = int(input(f'Qual é a soma de {a2} + {b2} = '))
if resp2 == (a2 + b2):
    acerto2 = 1
    erro2 = 0
    print('Parabens Você acertou')
else:
    erro2 = 1
    acerto2 = 0
    print(f'Você errou a resposta {erro2}')

a3 = choice(range(1, 100))
b3 = choice(range(1, 100))
c3 = a3 + b3
resp3 = int(input(f'Qual é a soma de {a3} + {b3} = '))
if resp3 == (a3 + b3):
    acerto3 = 1
    erro3 = 0
    print('Parabens Você acertou')
else:
    erro3 = 1
    acerto3 = 0
    print(f'Você errou a resposta {erro3}')

a4 = choice(range(1, 100))
b4 = choice(range(1, 100))
c4 = a4 + b4
resp4 = int(input(f'Qual é a soma de {a4} + {b4} = '))
if resp4 == (a4 + b4):
    acerto4 = 1
    erro4 = 0
    print('Parabens Você acertou')
else:
    erro4 = 1
    acerto4 = 0
    print(f'Você errou a resposta {erro4}')

print(f'A primeira pergunta foi a soma dos números {a} + {b} você respondeu {resp} e a resposta é = {c}')
print(f'A segunda pergunta foi a soma dos números {a1} + {b1} você respondeu {resp1} e a resposta é = {c1}')
print(f'A segunda pergunta foi a soma dos números {a2} + {b2} você respondeu {resp2} e a resposta é = {c2}')
print(f'A segunda pergunta foi a soma dos números {a3} + {b3} você respondeu {resp3} e a resposta é = {c3}')
print(f'A segunda pergunta foi a soma dos números {a4} + {b4} você respondeu {resp4} e a resposta é = {c4}')

somas = (acerto + acerto1 + acerto2 + acerto3 + acerto4)
erros = (erro + erro1 + erro2 + erro3 + erro4)

if somas > erros:
    print(f'Você acertou {somas} respostas das cinco perguntas')
else:
    print(f'Você errou {erros} respostas das cinco perguntas')
"""

"""
30 - Faça um programa que receba três números e mostre-os em ordem crescente.

num1 = int(input('Informe o primeiro núemro '))
num2 = int(input('Informe o segundo número '))
num3 = int(input('Informe o terceiro número '))

lista = [num1, num2, num3]
lista.sort()
print(f' Os números informados em ordem crescente são: {lista}')
"""

"""
31 - Faça um prgrama que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostra
qual a classificação dessa pessoa.

   ALTURA                                  PESO
                    Até 60      Entre 60 e 90 (Inclusive)   Acima de 90
Menor que 1,20         A                    D                      G
De 1,20 a 1,70         B                    E                      H
Maior que 1,70         C                    F                      I 


altura = float(input('Informe a altura da pessoa: '))
peso = float(input('Informe o peso da pessoa: '))


# Condição Altura menor que 1.20:

if altura < 1.20 and peso <= 60:
    pessoa = ('A')
    print(f'A pessoa obteve a classificação {pessoa}')

elif altura < 1.20 and peso > 60 and peso <= 90:
    pessoa = ('D')
    print(f'A pessoa obteve a classificação {pessoa}')

elif altura < 1.20 and peso > 90:
    pessoa = ('G')
    print(f'A pessoa obteve a classificação {pessoa}')


# Condição Altura de 1.20 até 1.70:

elif altura >= 1.20 and altura <= 1.70 and peso <= 60:
    pessoa = ('B')
    print(f'A pessoa obteve a classificação {pessoa}')

elif altura >= 1.20 and altura <= 1.70 and peso > 60 and peso <= 90:
    pessoa = ('E')
    print(f'A pessoa obteve a classificação {pessoa}')

elif altura >= 1.20 and altura <= 1.70 and peso > 90:
    pessoa = ('H')
    print(f'A pessoa obteve a classificação {pessoa}')


# Condição Altura maior que 1.70:

elif altura > 1.70 and peso <= 60:
    pessoa = ('C')
    print(f'A pessoa obteve a classificação {pessoa}')

elif altura > 1.70 and peso > 60 and peso <= 90:
    pessoa = ('F')
    print(f'A pessoa obteve a classificação {pessoa}')

elif altura > 1.70 and peso > 90:
    pessoa = ('I')
    print(f'A pessoa obteve a classificação {pessoa}')
"""

"""
32 - Escreva um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um 
pedido. O cardápio da lanchonete segue o padrão abaixo:

    Especificação       Código      Preço
Cachorro Quente         100         1.20
Bauru Simples           101         1.30
Bauru com Ovo           102         1.50
Hamburguer              103         1.20
Cheeserburguer          104         1.70
Suco                    105         2.20
Refrigerante            106         1.00

####

cardapio = ('Especificação          Código       Preço\n'            
            'Cachorro Quente         100         1.20\n'
            'Bauru Simples           101         1.30\n'
            'Bauru com Ovo           102         1.50\n'
            'Hamburguer              103         1.20\n'
            'Cheeserburguer          104         1.70\n'
            'Suco                    105         2.20\n'
            'Refrigerante            106         1.00' )
print(cardapio)

lista = ['Cachorro Quente', 'Bauru Simples', 'Bauru com Ovo', 'Hamburguer', 'Cheeserburguer', 'Suco', 'Refrigerante']
pedido = float(input('Dado o cardapio acima informe o código do produto desejado: '))

qtd = float(input('Informe a quantidade desejada: '))

if pedido == 100:
    pedido = qtd * 1.20
    lista = lista[0]
    print(f'Seu pedido foi de {qtd:.0f} {lista} e obteve o valor total de R$ {pedido:.2f}')

elif pedido == 101:
    pedido = qtd * 1.30
    lista = lista[1]
    print(f'Seu pedido foi de {qtd:.0f} {lista} e obteve o valor total de R$ {pedido:.2f}')

elif pedido == 102:
    pedido = qtd * 1.50
    lista = lista[2]
    print(f'Seu pedido foi de {qtd:.0f} {lista} e obteve o valor total de R$ {pedido:.2f}')

elif pedido == 103:
    pedido = qtd * 1.20
    lista = lista[2]
    print(f'Seu pedido foi de {qtd:.0f} {lista} e obteve o valor total de R$ {pedido:.2f}')

elif pedido == 104:
    pedido = qtd * 1.70
    lista = lista[3]
    print(f'Seu pedido foi de {qtd:.0f} {lista} e obteve o valor total de R$ {pedido:.2f}')

elif pedido == 105:
    pedido = qtd * 2.20
    lista = lista[4]
    print(f'Seu pedido foi de {qtd:.0f} {lista} e obteve o valor total de R$ {pedido:.2f}')

elif pedido == 106:
    pedido = qtd * 1.00
    lista = lista[5]
    print(f'Seu pedido foi de {qtd:.0f} {lista} e obteve o valor total de R$ {pedido:.2f}')

else:
    print(' ')
    print('O código informado não corresponde ao cardápio!!')

"""

"""
33 - Um produto vai sofrer aumento de acordo com a tabela abaixo, Leia o preço antigo, calcule e escreva o preço novo,
e escreva uma mensagem em função do preço novo (de acordo com a segunda taleba).

PREÇO ANTIGO                        PERCENTUAL DE AUMENTO
até R$ 50                                   5%
entre R$ 50 e R$ 100                        10%
acima de R$ 100                             15%

PREÇO NOVO                               MENSAGEM
até R$ 80                                 Barato
entre R$ 80 e R$ 120 (Incluisive)         Normal
entre R$ 120 e R$ 200 (Inclusive)          Caro
acima de R$ 200                         Muito caro  


produto = float(input('Informe o preço antigo do produto: '))
perc_5 = (produto / 100) * 5
perc_10 = (produto / 100) * 10
perc_15 = (produto / 100) * 15

if produto <= 50:
    preco_novo = produto + perc_5
    print(preco_novo)
    if preco_novo <= 80:
        print('Produto Barato')
    elif preco_novo > 80 and preco_novo <= 120:
        print('Preço Normal')
    elif preco_novo > 120 and preco_novo <= 200:
        print('Caro')
    elif preco_novo > 200:
        print('Muito Caro')

elif produto > 50 and produto <= 100:
    preco_novo = produto + perc_10
    print(preco_novo)
    if preco_novo <= 80:
        print('Produto Barato')
    elif preco_novo > 80 and preco_novo <= 120:
        print('Preço Normal')
    elif preco_novo > 120 and preco_novo <= 200:
        print('Caro')
    elif preco_novo > 200:
        print('Muito Caro')

elif produto > 100:
    preco_novo = produto + perc_15
    print(preco_novo)
    if preco_novo <= 80:
        print('Produto Barato')
    elif preco_novo > 80 and preco_novo <= 120:
        print('Preço Normal')
    elif preco_novo > 120 and preco_novo <= 200:
        print('Caro')
    elif preco_novo > 200:
        print('Muito Caro')
"""

"""
34 - Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo, quando o 
aluno tem mais de 20 faltas ocorre uma redução de conceito.

    NOTA                CONCEITO (ATÉ 20 FALTAS)            CONCEITO (MAIS DE 20 FALTAS)
9.0 até 10.0                      A                                      B
7.5 até 8.9                       B                                      C
5.0 até 7.4                       C                                      D
4.0 até 4.9                       D                                      E
0.0 até 3.9                       E                                      E


nota = float(input('Informe a nota do aluno: '))
faltas = float(input('Informe o número de faltas do aluno: '))

if nota >= 9.0 and nota <= 10 and faltas > 0 and faltas <= 20:
    print(f'O aluno registrou {faltas:.0f} faltas e nota {nota:.0f}; sendo assim obteve o conceito = A')

elif nota >= 9.0 and nota <= 10 and faltas > 0 and faltas > 20:
    print(f'O aluno registrou {faltas:.0f} faltas e nota {nota:.0f}; sendo assim obteve o conceito = B')

elif nota >= 7.5 and nota < 9 and faltas > 0 and faltas <= 20:
    print(f'O aluno registrou {faltas:.0f} faltas e nota {nota:.0f}; sendo assim obteve o conceito = B')

elif nota >= 7.5 and nota < 9 and faltas > 0 and faltas > 20:
    print(f'O aluno registrou {faltas:.0f} faltas e nota {nota:.0f}; sendo assim obteve o conceito = C')

elif nota >= 5.0 and nota < 7.5 and faltas > 0 and faltas <= 20:
    print(f'O aluno registrou {faltas:.0f} faltas e nota {nota:.0f}; sendo assim obteve o conceito = C')

elif nota >= 5.0 and nota < 7.5 and faltas > 0 and faltas > 20:
    print(f'O aluno registrou {faltas:.0f} faltas e nota {nota:.0f}; sendo assim obteve o conceito = D')

elif nota >= 4.0 and nota < 5.0 and faltas > 0 and faltas <= 20:
    print(f'O aluno registrou {faltas:.0f} faltas e nota {nota:.0f}; sendo assim obteve o conceito = D')

elif nota >= 4.0 and nota < 5.0 and faltas > 0 and faltas > 20:
    print(f'O aluno registrou {faltas:.0f} faltas e nota {nota:.0f}; sendo assim obteve o conceito = E')

elif nota >= 0.0 and nota < 5.0 and faltas > 0 and faltas <= 20:
    print(f'O aluno registrou {faltas:.0f} faltas e nota {nota:.0f}; sendo assim obteve o conceito = E')

elif nota >= 0.0 and nota < 5.0 and faltas > 0 and faltas > 20:
    print(f'O aluno registrou {faltas:.0f} faltas e nota {nota:.0f}; sendo assim obteve o conceito = E')

else:
    print('Valor da nota ou número de faltas não atende a regra estabelecida!! -  NECESSÁRIO CORRIGIR')
"""

"""
35 - Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe
naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.

dia = float(input('Informe o dia: '))
mes = float(input('Informe o mês: '))
ano = float(input('Informe o ano: '))

if mes == 1 and dia > 0 and dia <= 31:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Janeiro')

elif mes == 2:
    if ano % 4 == 0 and ano % 100 != 0 and dia > 1 and dia <= 29:
        print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} (Ano Bissexto)')
    else:
        print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} (Ano não é Bissexto)')

elif mes == 3 and dia > 0 and dia <= 31:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Março')

elif mes == 4 and dia > 0 and dia <= 30:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Abril')

elif mes == 5 and dia > 0 and dia <= 31:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Maio')

elif mes == 6 and dia > 0 and dia <= 30:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Junho')

elif mes == 7 and dia > 0 and dia <= 31:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Julho')

elif mes == 8 and dia > 0 and dia <= 31:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Agosto')

elif mes == 9 and dia > 0 and dia <= 30:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Setembro')

elif mes == 10 and dia > 0 and dia <= 31:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Outubro')

elif mes == 11 and dia > 0 and dia <= 30:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Novembro')

elif mes == 12 and dia > 0 and dia <= 31:
    print(f'A data informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - Dezembro')

else:
    print('!!!! Data informada não é valida  !!!')
"""

"""
36 - Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para 
calcular a comissão, considere a tabela abaixo:

        VENDA MENSAL                                        COMISSÃO
Maior ou igual a R$ 100.000,00                      R$ 700,00 + 16% das vendas
Menor que 80.000,00 ou igual a R$ 60.000,00         R$ 650,00 + 14% das vendas
Menor que 60.000,00 ou igual a R$ 40.000,00         R$ 550,00 + 14% das vendas
Menor que 40.000,00 ou igual a R$ 20.000,00         R$ 500,00 + 14% das vendas
Menor que R$ 20.000,00                              R$ 400,00 + 14% das vendas

venda = float(input('Informe o valor da venda R$ '))
percentual = venda / 100
comissao = [16, 14]
salarios = [700, 650, 550, 500, 400]

if venda >= 100_000:
    comissao = (salarios[0] + (percentual * comissao[0]))
    print(f' O valor a ser pago de comissão é R$ {comissao:.2f} - Venda acima de R$ 100.000,00')

elif venda < 80_000 and venda >= 60_000:
    comissao = (salarios[1] + (percentual * comissao[1]))
    print(f' O valor a ser pago de comissão é R$ {comissao:.2f} - Venda entre R$ 80.000,00 e R$ 60.000,00')

elif venda < 60_000 and venda >= 40_000:
    comissao = (salarios[2] + (percentual * comissao[1]))
    print(f' O valor a ser pago de comissão é R$ {comissao:.2f} - Venda entre R$ 60.000,00 e R$ 40.000,00')

elif venda < 40_000 and venda >= 20_000:
    comissao = (salarios[3] + (percentual * comissao[1]))
    print(f' O valor a ser pago de comissão é R$ {comissao:.2f} - Venda entre R$ 40.000,00 e R$ 20.000,00')

elif venda < 20_000:
    comissao = (salarios[3] + (percentual * comissao[1]))
    print(f' O valor a ser pago de comissão é R$ {comissao:.2f} - Venda abaixo de R$ 20.000,00')
"""

"""
37 - As tarifas de certo parque de estacionamento são as seguintes:
    1ª e 2ª hora - R$ 1,00 cada
    3ª e 4ª hora - R$ 1,40 cada
    5ª horas seguintes - R$ 2,00 cada
    
O número de horas é sempre inteiro e arredondado por execesso. Deste modo, quem estacionar durante 61 minutos paragrá
por duas, que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque é apartida
deste são apresentados na forma de pares de inteiros, representados horas e minutos. Por exemplo, o par 12 50
representa 10 para uma da tarde". Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e de
partida se dão com o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com intervalo não
superior a 24 horas. Portanto, se uma data hora de chegada for superior à de partida, isso não é uma situação de erro,
antes significará que a partida ocorreu no dia seguinte ao de chegada.


import  math


chegada = list(input('Informe a data e horário de chegada (dd-mm-aaaa_hh:mm): '))
saida = list(input('Informe a data e horário de chegada (dd-mm-aaaa_hh:mm): '))


#Recebimento dia, hora e minutos no formato lista:
d_chegada = chegada[0] + chegada[1]
h_chegada = chegada[11] + chegada[12]
m_chegada = chegada[14] + chegada[15]

d_saida = saida[0] + saida[1]
h_saida = saida[11] + saida[12]
m_saida = saida[14] + saida[15]

# Transformação do dia, hora e minutos para o formato float:
dia_cheg = float(d_chegada)
hora_cheg = float(h_chegada)
min_cheg = float(m_chegada)

dia_saida = float(d_saida)
hora_saida = float(h_saida)
min_saida = float(m_saida)

# Declaração das taxas
taxa1 = 1 # 1ª e 2ª hora
taxa2 = 1.40 # 3ª e 4ª hora
taxa3 = 2 # apartir da 5ª hora

# Cálculo do tempo e valor a ser pago referente o uso do estacionamento:

# Opção dentro da mesma hora de chegada:
if dia_cheg == dia_saida and hora_saida == hora_cheg:
    min_uso = (min_saida - min_cheg)
    print(min_uso)

    uso_total_horas = math.ceil(float(min_uso / 60))

    pagar = math.ceil(uso_total_horas) * taxa1
    print(f' O tempo de permancia no estacionamento foi de {uso_total_horas} sendo assim o valor é = R$ {pagar:.2f}\n'
          'o tempo em horas foi arredondado para cima')

# Opção dentro da hora de chegada e a hora posterior a de chegada:
elif dia_cheg == dia_saida and hora_saida == (hora_cheg + 1):
    min_uso = (60 - min_cheg) + (min_saida)

    uso_total_horas = math.ceil(float(min_uso / 60))

    pagar = math.ceil(uso_total_horas) * taxa1
    print(f' O tempo de permancia no estacionamento foi de {uso_total_horas} sendo assim o valor é = R$ {pagar:.2f}\n'
          'o tempo em horas foi arredondado para cima')

# Opção dentro do mesmo dia e apartir da hora posterior a de chegada:
elif dia_cheg == dia_saida and hora_saida > (hora_cheg + 1):
    min_uso = ((hora_saida * 60) + (min_saida)) - ((hora_cheg * 60) + (min_cheg))

    uso_total_horas = float(min_uso / 60)

    if min_uso > 120 and min_uso <= 240:
        pagar = math.ceil(uso_total_horas)
        taxa_parcial_1 = 2 * taxa1 + (pagar - 2) * taxa2
        print(
            f' O tempo de permancia no estacionamento foi de {uso_total_horas} sendo assim o valor é = R$ {taxa_parcial_1:.2f}\n'
            'o tempo em horas foi arredondado para cima')

    else:
        pagar = math.ceil(uso_total_horas)
        taxa_parcial_1 = 2 * taxa1 + 2 * taxa2 + (pagar - 4) * taxa3

        print(
            f' O tempo de permancia no estacionamento foi de {uso_total_horas} sendo assim o valor é = R$ {taxa_parcial_1:.2f}\n'
            'o tempo em horas foi arredondado para cima')

# Opção para saída no dia posterior ao de chegada:
elif dia_saida == dia_cheg + 1:
    tempo_uso = (((24-hora_cheg)*60) + min_cheg) + (hora_saida * 60) + (min_saida)

    uso_total_horas = float(tempo_uso / 60)

    pagar = math.ceil(uso_total_horas)

    taxa_parcial_2 = 2 * taxa1 + 2 * taxa2 + (pagar - 4) * taxa3

    print(
        f' O tempo de permancia no estacionamento foi de {uso_total_horas} sendo assim o valor é = R$ {taxa_parcial_2:.2f}\n'
        'o tempo em horas foi arredondado para cima')

# Opção para saída após o dia posterior ao de chegada (Ex. 3 dias):
elif dia_saida > dia_cheg + 1:
    tempo_uso = (((24 - hora_cheg) * 60) + min_cheg) + ((dia_saida - (dia_cheg + 1))*24)*60

    uso_total_horas = float(tempo_uso / 60)

    pagar = math.ceil(uso_total_horas)

    taxa_parcial_2 = 2 * taxa1 + 2 * taxa2 + (pagar - 4) * taxa3

    print(
        f' O tempo de permancia no estacionamento foi de {uso_total_horas} sendo assim o valor é = R$ {taxa_parcial_2:.2f}\n'
        'o tempo em horas foi arredondado para cima')

else:
    print('Dados informados não correspondem a regra (Revisar formato de intrudução, datas chegada, saída e\n'
          'horas de chegada e saída')
"""

"""
38 - Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros:
Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma data válida. Teste se dia fornecido é um dia 
válido: dia > 0, dia <= 28 para mês de fevereiro (29 se o ano for bissexto), dia <= 30 em abril, julho, setembro e 
novembro, dia <= 31 nos outros meses. Teste a validade do mês > 0 e mês < 13. Teste a validade do ano: ano <= ano atual
(use uma constante definida com o valor igual a 2008). Imprimir: "data válida" ou "data invalida" no final da execução
do programa.


# Coletando a data em formato de lista:
data = list(input('Informe a data de nascimento (dd-mm-aaaa):'))

# Transformando a data em inteiro e separando dia, mês e ano em variaveis:
dia = int(data[0] + data[1])
mes = int(data[3] + data[4])
ano = int(data[6] + data[7] + data[8] + data[9])

# Testando se as datas são validas:
if mes == 4 or mes == 6 or mes == 11 and dia >= 1 and dia <= 30 and ano <= 2020:
    if mes == 1 and dia > 0 and dia <= 31:
        print(f'A data de nascimento informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - DATA VÁLIDA')

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 9 or mes == 10 or mes == 12 and dia >= 1 and \
        dia <= 31 and ano <= 2020:
    if mes == 1 and dia > 0 and dia <= 31:
        print(f'A data de nascimento informada é {dia:.0f}/{mes:.0f}/{ano:.0f} - DATA VÁLIDA')

elif ano % 4 == 0 and ano % 100 != 0 and dia >= 1 and dia <= 29 and ano <= 2020:
        print(f'A data de nascimento informada é {dia:.0f}/{mes:.0f}/{ano:.0f} (Ano Bissexto) - DATA VÁLIDA')

elif ano % 4 != 0 and ano % 100 == 0 and dia >= 1 and dia <= 28 and ano <= 2020:
        print(f'A data de nascimento informada é {dia:.0f}/{mes:.0f}/{ano:.0f} (Ano não é Bissexto) - DATA VÁLIDA')

else:
    print('DATA NÃO É VÁLIDA')
"""

"""
39 - Um a empresa decide dar um aumento aos funcionários de acordo com uma tabela que considera o salário atual e o 
tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior do que
os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus
adicional de salário. Faça um programa que leia:

    -   O valor do salário atual do funcionário;
    -   O tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final
reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

            SALÁRIO ATUAL           REAJUSTE(%)         TEMPO DE SERVIÇO            BÔNUS
            Até 500,00                  25%              Abaixo de 1 ano           Sem bônus
            Até 1.000,00                20%              De 1 a 3 anos               100,00
            Até 1.500,00                15%              De 4 a 6 anos               200,00
            Até 2.000,00                10%              De 7 a 10 anos              300,00
         Acima de 2.000,00          Sem Reajuste         Mais de 10 anos             500,00
         

salario = float(input('Informe o salário atual do funcionário R$ '))
tempo_serv = float(input('Informe quanto tempo de serviço tem o funcionário (Anos): '))

reajuste = [0.25, 0.20, 0.15, 0.10]

bonus = [100, 200, 300, 500]

if salario <= 500 and tempo_serv < 1:

    novo_salario = salario + (float(reajuste[0]) * salario)
    print(f'O funcionário tem um salario atual de R$ {salario} e {tempo_serv:.0f} anos de tempo de serviço sendo assim'
          f'obtive um aumento de {((float(reajuste[0])) * 100):.0f}% passando para um novo salário de '
          f'R$ {novo_salario:.2f}')

elif salario <= 1000 and tempo_serv >= 1 and tempo_serv < 4:

    novo_salario = salario + (float(reajuste[1]) * salario) + (float(bonus[0]))
    print(f'O funcionário tem um salario atual de R$ {salario:.2f} e {tempo_serv:.0f} anos de tempo de serviço sendo '
          f'assim obtive um aumento de {((float(reajuste[1])) * 100):.0f}% e R$ {float(bonus[0]):.2f} de bonus passando '
          f'para um novo salário de R$ {novo_salario:.2f}')

elif salario <= 1500 and tempo_serv >= 4 and tempo_serv < 7:

    novo_salario = salario + (float(reajuste[2]) * salario) + (float(bonus[1]))
    print(f'O funcionário tem um salario atual de R$ {salario:.2f} e {tempo_serv:.0f} anos de tempo de serviço sendo '
          f'assim obtive um aumento de {((float(reajuste[2])) * 100):.0f}% e R$ {float(bonus[1]):.2f} passando para um '
          f'novo salário de R$ {novo_salario:.2f}')

elif salario <= 2000 and tempo_serv >= 7 and tempo_serv <= 10:

    novo_salario = salario + (float(reajuste[3]) * salario) + (float(bonus[2]))
    print(f'O funcionário tem um salario atual de R$ {salario:.2f} e {tempo_serv:.0f} anos de tempo de serviço sendo '
          f'assim obtive um aumento de {((float(reajuste[3])) * 100):.0f}% e R$ {float(bonus[2]):.2f} passando para um '
          f'novo salário de R$ {novo_salario:.2f}')

elif salario > 2000 and tempo_serv > 10:

    novo_salario = salario + (float(bonus[3]))
    print(f'O funcionário tem um salario atual de R$ {salario:.2f} e {tempo_serv:.0f} anos de tempo de serviço sendo '
          f'assim obtive um bonus de R$ {float(bonus[2]):.2f} passando para um novo salário de R$ {novo_salario:.2f}')

else:
    print('REVEJA OS DADOS INFORMADOS NÃO ATENDE A REGRA PARA REAJUSTE SALARIAL.')
"""

"""
40 - O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos.
A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica
e escreva o custo ao consumidor.

        CUSTO DE FÁBRICA                % DO DISTRIBUIDOR               % DOS IMPOSTOS
        Até R$ 12.000,00                      5                            Insento
   Entre R$ 12.000,00 e 25.000,00             10                              15
   Acima de R$ 25.000,00                      15                              20

custo_fab = float(input('Informe o custo de fabrica R$ '))
dist_5 = .05
dist_10 = .10
dist_15 = .15
impos_15 = .15
impos_20 = .20

if custo_fab > 0 and custo_fab < 12_000:
    custo_cons = custo_fab + (custo_fab * dist_5)
    print(f'O custo do carro para o consumidor é R$ {custo_cons:.2f}')

elif custo_fab >= 12_000.00 and custo_fab <= 25_000.00:
    custo_cons = custo_fab + (custo_fab * dist_10) + (custo_fab * impos_15)
    print(f'O custo do carro para o consumidor é R$ {custo_cons:.2f}')

elif custo_fab > 25_000.00:
    custo_cons = custo_fab + (custo_fab * dist_15) + (custo_fab * impos_20)
    print(f'O custo do carro para o consumidor é R$ {custo_cons:.2f}')

else:
    print('VALOR INFORMADO FORA DA REGRA ESTABELECIDA !!! ')
"""

"""
41 - Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

            IMC                         CLASSIFICAÇÃO
           < 18,5                       Abaixo do Peso
           18,6 - 24,9                  Saudável
           25,0 - 29,9                  Peso em excesso
           30,0 - 34,9                  Obsidade Grau I
           35,0 - 39,9                  Obsidade Grau II (severa)
           >= 40,0                      Obsidade Grau III (mórbida)


peso = float(input('Informe o peso da pessoa (kg):'))
altura = float(input('Informe a altura da pessoa (metro):'))
imc = peso / (altura**2)

if imc >0 and imc <= 18.5:
    print(f'O peso informado foi {peso:.0f}kg a altura é {altura:.2f}m assim a pessoa tem o IMC de {imc:.0f} e está '
          f'abaixo do peso')

elif imc > 18.5 and imc < 25:
    print(f'O peso informado foi {peso:.0f}kg a altura é {altura:.2f}m assim a pessoa tem o IMC de {imc:.0f} e está '
          f'saudável')

elif imc > 25 and imc < 30:
    print(f'O peso informado foi {peso:.0f}kg a altura é {altura:.2f}m assim a pessoa tem o IMC de {imc:.0f} e está com'
          f' peso em excesso')

elif imc > 30 and imc < 35:
    print(f'O peso informado foi {peso:.0f}kg a altura é {altura:.2f}m assim a pessoa tem o IMC de {imc:.0f} e está com'
          f' Obsidade Grau I')

elif imc > 35 and imc < 40:
    print(f'O peso informado foi {peso:.0f}kg a altura é {altura:.2f}m assim a pessoa tem o IMC de {imc:.0f} e está com'
          f' Obsidade Grau II (severa)')

elif imc >= 40:
    print(f'O peso informado foi {peso:.0f}kg a altura é {altura:.2f}m assim a pessoa tem o IMC de {imc:.0f} e está com'
          f' Obsidade Grau III (mórbida)')

else:
    print(f'O peso informado foi {peso:.0f}kg a altura é {altura:.2f}m ssim a pessoa tem o IMC de {imc:.0f} - REVEJA AS'
          f' INFORMAÇÕES ESTÃO FORA DA REGRA ESTABELECIDA !!!')
"""

