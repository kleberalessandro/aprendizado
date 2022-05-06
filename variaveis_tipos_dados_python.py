####   CÓDIGOS DE CONHECIMENTOS BÁSICOS SOBRE VÁRIAVEIS E TIPOS DE DADOS   ####
'''
1 - Faça um programa que leia um número inteiro e o imprima.
'''
numero = 10.0
print(numero)
print()


'''
2 - Faça um programa que leia um número real e imprima.
'''
numero = 10.0
print(numero)
print(type(numero))
numero_inteiro = int(numero)
print(numero_inteiro)
print(type(numero_inteiro))
print()


'''
3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
'''
num_int_1 = int(input('Informe o primeiro número inteiro? '))
num_int_2 = int(input('Informe o segundo número inteiro? '))
num_int_3 = int(input('Informe o terceiro número inteiro? '))
soma = num_int_1 + num_int_2 + num_int_3
print('A soma dos números informados: ', num_int_1, ',', num_int_2, 'e', num_int_3, 'é =', soma)
print()


'''
4 - Leia um número real e imprima o resultado do quadrado desse número.
'''
num_real = float(input('Informe um número real: '))
quad_num_real = (num_real**2)
print('O número informado foi: ', num_real, 'e o quadrado  é: ', quad_num_real)
print()


'''
5 - Leia um número real e imprima a quinta parte deste número
'''
num = float(input('Informe um número inteiro: '))
num_5parte = float(num/(5))
print('O número informado foi: ', num, ';e a quinta parte é:', num_5parte)
print()


'''
6 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
Formula de Conversão é: F = C*(90/5.0) + 32.0, sendo F a temperatura em Celsius e F a temperatura em Fahrenheit.
'''
temp_celsius = float(input('Informe a temperatura em graus Celsius? '))
print(type(temp_celsius))
temp_fahrenheit = temp_celsius*(float(9/5)) + 32
print('A temperatura informada convertida em Fhrenheit é=', temp_fahrenheit,'°F')
print(type(temp_fahrenheit))
print()


'''
7 - Leia uma temperatura em graus Fahrenheit e apresente-a em graus Celsius. A fórmula de conversão é: 
C = 5.0*(F-32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
'''

temp_fahrenheit = float(input('Qual a temperatura em graus Fahrenheit? '))
temp_celsius = (float(5*(temp_fahrenheit-32)/9))
print(f'A temperatura em graus Celsius é: {temp_celsius:.2f}°C')
print()


'''
8 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é:
 C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em kelvin.
'''
temp_kelvin = float(input('Informe a temperatura em graus Kelvin? '))
temp_celsius = float(temp_kelvin-273.15)
print(f'A temperatura em graus Celsius é: {temp_celsius:.2f}°C')
print()


'''
9 - Leia uma temperatura em graus Celsius e apresente-a convertida em Kelvin. A fórmula de conversão é: K = C + 273,
sendo C a temperatura em Celsius e K a temperatura em Kelvin
'''
temp_celsius = float(input('Informe a temperatura em graus Celsius? '))
temp_kelvin = float(temp_celsius + 273.15)
print(f'A temperatura em graus Kelvin é: {temp_kelvin:.2f}K')


'''
10 - Leia a velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula de
conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.
'''
veloc_kmh = float(input('Informe a velocidade em km/h? '))
veloc_ms = float(veloc_kmh/3.6)
print('A velocidade em m/s é: ', round(veloc_ms),'m/s')


'''
11 - Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora). A fórmula
de conversão é K = M * 3.6, sendo K a velocidad em kkm/h e M em m/s.
'''
m = float(input('Qual a velocidade em m/s? '))
k = float(m * 3.6)
print('A velocidade em m/s é: ',k,'km/h')

'''
12 - Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é: K = 1,61 * M, sendo
K a distância em quilômetros e M em milhas.
'''
m = float(input('Informe a distânica em milhas? '))
k = float(m * 1.61)
print(f'Distância em milhas informada = {m:.2f} a distância em Km/h é = {k:.2f}')


'''
13 - Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de conversão é M = K/1,61, sendo 
K a distância em quilômetros e M em milhas.
'''
k = float(input('Informe a distância em quilômetros? '))
m = float(k / 1.61)
print(f'A distância informada em quilometros foi = {k:.2f} em milhas é = {m:.2f}')


'''
14 - Leia um ângulo em graus e apresente-o convertido em radios. A fórmula de conversão é R = G * pi/180, sendo 
G o ângulo em graus e R em radianos e pi = 3.14.
'''
angulo = float(input('Informe qual o ângulo em graus: '))
print(type(angulo))
radianos = angulo*(3.14/180)
print(f'O ângulo informa em graus foi: {angulo:.0f}º em radianos é = {radianos:.2f} radian')


'''
15 - Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é G = R * 180/pi, sendo 
G o ângulo em graus e R em radianos e pi = 3.14.
'''
r = float(input('Informe qual é o ânulo em radianos: '))
g = float(r*(180/3.14))
print(f'O angulo informado em radianos foi: {r:.2f} em graus é = {round(g)}º')


'''
16 - Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros. A fórmula de conversão é:
C = P * 2,54, sendo C o comprimento em centimentros e P o comprimento em polegadas.
'''
p = float(input('Informe o comprimento em polegada:'))
c = float(p * 2.54)
print(f'O valor do comprimento informado em polegadas foi: {p:.1f} em centimetros é = {c:.2f} cm')


'''
17 - Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas. A fórmula de conversão é:
P = C / 2,54, sndo C o comprimento em centimetros e P o comprimento em polegadas
'''
c = float(input('Informe o comprimento em centimetros:'))
p = float(c / 2.54)
print(f'O valor em polegada é = ', round(p),"'")


'''
18 - Leia um valor em metros cúbicos m³ e apresente-o convertido em litros. A fórmula de conversão é: L = 100 * M,
sendo L o volume em litros e M o volume em metros cúbicos.
'''
m = float(input('Informe o valor em M³: '))
l = m * 1000.0
print(f'O valor em M³ informado foi = {int(m)} em litros é = {int(l)} litros')


'''
19 - Leia um valor de volume em litros e apresente-o em metros cúbicos m³. A fórmula de conversão é: M = L / 1000,
sendo L o volume em litros e M o volume em metros cúbicos.
'''
l = float(input('Qual o volume em litros? '))
m = l / 1_000
print('O volume em m³ é = ',int(m),'m³')


'''
20 - Leia um valor de massa em quilograma e apresente-o convertido em libras. A fórmula de conversão é: L = K / 0,45,
sendo K a massa em quilograma e L a massa em libras.
'''
k = float(input('Qual a massa em Kg? '))
l = k / 0.45
print('A massa em libras é:',round(l),'libras')


'''
21 - Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é: K = L * 0,45,
sendo K a massa em quilogramas e L a massa em libras.
'''


'''
22 - Leia um valor em jardas e apresente-o convertido em metros. A fórmula de conversão é: M = 0,91 * J, sendo
J o comprimento em jardas e M o comprimento em metros.
'''
j = float(input('Qual o valor em Jardas? '))
m = 0.91 * j
print(f'O valor em metros é = {round(m)}m')


'''
23 - Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula de conversão é: J = M / 0,91,
sendo J o comprimento em jardas e M o comprimento em metros.
'''
m = float(input('Qual o valor em metros? '))
j = m / 0.91
print('O valor em Jardas é ={round(j)} Jardas')


'''
24 - Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A fórmula de conversão é: 
A = M * 0,000247, sendo M a área em metros quadrados e A a área em acres.
'''
m = float(input('Qual a área em m²? '))
a = m * 0.000247
print(f'A área em acres é = {a} acres')


'''
25 - Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A fórmula de conversão é: 
M = A * 4048,58, sendo M a área em metros quadrados e A a área em acres.
'''
a = float(input('Qual a área em Acres? '))
m = a * 4048.58
print(f'A área em m² é = {m} m²')


'''
26 - Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares. A fórmula de conversão é:
H = M * 0,0001, sendo M a área em matros quadradps e H a área em hectares.
'''
m = float(input('Qual é a área m²?'))
h = m * 0.0001
print(f'A área em hectáres é = {h} hectares')


'''
27 - Leia um valor de área em hectares e apresente-o convertido em metros quadrados m². A fórmula de conversão é:
M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.
'''
h = float(input('Qual é a área em hectares? '))
m = h* 1_0000
print(f'A área em metros quadrado é = {m:.1f}m²')


'''
28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
'''
valor1 = float(input('Informe o 1º valor: '))
valor2 = float(input('Informe o 1º valor: '))
valor3 = float(input('Informe o 1º valor: '))

quadrado_valor1 = valor1**2
quadrado_valor2 = valor2**2
quadrado_valor3 = valor3**2
soma_quadrado_valores = quadrado_valor1 + quadrado_valor2 + quadrado_valor3
print(soma_quadrado_valores)


'''
29 - Leia quatro notas, calcule a média aritmética e imprima o resultado
'''
nota1 = float(input('Qual a 1ª nota? '))
nota2 = float(input('Qual a 2ª nota? '))
nota3 = float(input('Qual a 3ª nota? '))
nota4 = float(input('Qual a 4ª nota? '))

media_notas = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média das notas é = {media_notas:.1f}')


'''
30 - Leia um valor real e a cotação do dólar. Em seguida, impprima o valor correspondete em dólares.
'''
real = float(input('Informe o valor em real? '))
cotação_dolar = float(input('Informe a cotação do dolar?'))
valor_real_x_dolar = real * cotação_dolar
print(f'O valor em real x dolar é = R$ {valor_real_x_dolar:.2f}')


'''
31 - Leia um número inteiro e imprima o seu secessor
'''
num_inteiro = int(input('Qual o número inteiro? '))
antecessor = int(num_inteiro - 1)
sucessor = int(num_inteiro + 1)
print(f'O número antecessor ao número inteiro informado é = {antecessor}')
print(f'O número sucessor ao número inteiro informado é = {sucessor}')


'''
32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
'''
num_int = int(input('Qual o número inteiro? '))
suc_tri_num = (num_int * 3) + 1
ant_dob_num = (num_int * 2) - 1
soma_suc_ant = suc_tri_num + ant_dob_num
print(f'A soma do sucessor do triplo e antecessor do dobro do número informado é = {soma_suc_ant}')


'''
33 - Leia a soma do lado de um quadrado e imprima como resultado a sua área.
'''
lado = float(input('Qual é a tamanho do lado do quadrado? '))
area = lado **2
print(f'A área do quadrado é = {area}')


'''
34 - Leia o valor do raio de circulo e calcule e imprima a área do círculo correspondente. A área do círculo é 
pi * raio², considere pi = 3.141592
'''
raio = float(input('Qual é o raio do circulo? '))
area = raio * 3.141592
print(f'A área do circulo é = {area:.2f}')


'''
35 - Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = raiz(a² + b²). faça
um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa
operação.
'''
a = float(input('Informe o valor do cateto a? '))
a2 = a **2
b = float(input('Informe o valor do cateto b? '))
b2 = b **2
hip = (a2 + b2) **1/2
print(f'O valor da hipotenusa da equação é = {hip}')


'''
36 - Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro é calculado
por meio da seguinte fórmula: V = pi * raio² * altura, onde pi = 3.141592.
'''
altura = float(input('Qual a altura do cilindro? '))
raio = float(input('Qual o raio do cilindro? '))
pi = 3.141592
volume = pi * (raio **2) * altura
print(f'O volume do cilindro é = {volume:.2f}')


'''
37 - Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto
foi 12%
'''
valor = float(input('Qual o valor do produto? '))
valor_desc = valor - (valor * 0.12)
print(f'O valor do produto com desconto é = R${valor_desc:.2f}')


'''
38 - Leia o salário de um funcionario. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de
25%.
'''
salario = float(input('Qual o salário do funcionario? '))
salario_reaj = (salario * 0.25) + salario
print(f'O novo salário com reajuste de 25% é = R$ {salario_reaj:.2f}')


'''
39 - A importancia de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:

- O primeiro ganhador recebeu 46%;
- O segundo receberá 32%;
- O tereceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
'''
premio = 780_000.00
ganhador1 = premio * 0.46
ganhador2 = premio * 0.32
ganhador3 = premio * (1-(0.46 + 0.32))
print(f'A quantia ganha pelo 1º ganhador é = R$ {ganhador1:.2f}\n'
      f'A quantia ganha pelo 2º ganhador é = R$ {ganhador2:.2f}\n'
      f'A quantia ganha pelo 3º ganhador é = R$ {ganhador3:.2f}')


'''
40 - Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados 
pelo encanador e imprima a quantia líquida que deverá ser paga, sandendo-se que são descontados 8% para imposto de renda
'''
valor_dia = 30.00
dias = float(input('Quantos dias o encanador trabalhou? '))
imposto = 0.08
liquido = (valor_dia - (valor_dia * imposto)) * dias
print(f'O valor líquido a receber é: R$ {liquido:.2f}')


'''
41 - Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. imprima o 
valor o valor a ser pago ao funcionário, adicione 10% sobre o valor calculado.
'''
valor_horas = float(input('Qual o valor da hora de trabalho? R$: '))
horas_trab = float(input('Qual a quantidade de horas trabalhadasno mês? '))
valor_trab_10 = (valor_horas * horas_trab) + ((valor_horas * horas_trab ) * 0.10)
print(f'O valor a ser pago ao funcionário adicionado 10% é = {valor_trab_10:.2f}')


'''
42 - Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem
uma gratificação de 5% sobre o sálario-base. Além disso ele paga 7% de imposto sobre o salário-base.
'''
salario_bas = float(input('Qual o salário-base do funcionário? R$ '))
gratificacao = 0.05
imposto = 0.07
salario_rec = salario_bas + (gratificacao * salario_bas) - (imposto * salario_bas)
print(f'O salário à receber do funcionário com a gratificação e deduzido o imposto é = R$ {salario_rec:.2f}')


'''
43 - Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
    -   O total a pagar com descontos de 10% ;
    -   O valor de cada parcela. no parcelamento de 3x sem juros;
    -   A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto);
    -   A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total).
'''
valor_total = float(input('Qual o valor total da venda? R$ '))
valor_desc_10 = valor_total - (valor_total * 0.10)
valor_parc_3x = valor_total / 3
valor_com_vista = valor_desc_10 * 0.05
valor_com_parc = valor_total * 0.05
print(f'O valor total a pagar com desconto de 10% é = R$ {valor_desc_10:.2f}\n'
      f'O valor de cada parcela, no parcelamento de 3x sem juros é = R$ {valor_parc_3x:.2f}\n'
      f'O valor da comissão do vendedor, no caso de venda ser a vista é = R$ {valor_com_vista:.2f}\n'
      f'O valor da comissão do vendedor, no caso da venda ser parcelada é = {valor_com_parc:.2f}\n')


'''
44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja alcaçar subindo a escada. Clacule e mostre
quantos degraus o usuário deverá subir para atingir seu objetivo.
'''
altura_degrau = float(input('Qual a altura em cm do degrau? '))
altura_total = float(input('Qual a altura total em metros? '))
altura_total_cm = altura_total * 100
qtd_degarus = altura_total_cm / altura_degrau
print(f'O total de degraus são = {qtd_degarus:.1f} degraus')


'''
45 - Faça um programa para converter uma letra maiúscula em uma letra minúscula. Use a tabela ASCII para resolver o 
problema.

Notas = Tabela ASCII padrão tem 256 caracteres mas no python tem muito mais ou seja ela tem a função chr exemplo:
'''
for i in range(257):
    print(f'ID: {i} Char: {chr(i)}') # chr passa um ID e a representação dele exemplo:
    print("------------------------") #Separador das linhas / caracteres da tabela
'''
Outra função é a ord só que ao contrario vc passa o carctere e ele informa o ID correspondente na tabela ASCII
Outra função é a sort que organiza as caracteres em ordem conforme o padrão da tabela ASCII

45 - Faça um programa para converter uma letra maiúscula em uma letra minúscula. Use a tabela ASCII para resolver o 
problema.
'''
letra = input('Qual é a letra maiuscula? ')
letraMinuscula = letra.lower()
print(f' A letra  minuscula é: {letraMinuscula}')


'''
46 - Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado
pelos dígitos invertido do número lido. Exemplo (Número = 123) (Número Gerado = 321)
'''
numero = int(input('Informe um numero entre 100 e 999? '))
novo_numero = ('O número não acima de 100')
novo_numero1 = ('O número não está abaixo de 999')
if numero > 100:
    novo_numero = ('O é acima de 100')
    if numero < 900:
        novo_numero1 = ('O número é abaixo de 999')


numero_str = str(numero)
numero_reverse = numero_str[::-1]
print((novo_numero),'e', (novo_numero1))

print('O número lido invertido é =', numero_reverse)


'''
48 - Leia um número inteiro 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
'''
num = int(input('Informe um número inteiro de 4 dígitos entre 1000 e 9999: '))
num1 = str(num)
print('',num1[0],'\n',num1[1],'\n',num1[2],'\n',num1[3])
#num_split = num1[0],[1]
#print(num_split)


'''
49 - Faça um programa que leia o horário (hora, minuto e segundo) de início e a duração, em segundos, de uma experiência
biologica. O pragrama deve resultar com o novo horário (hora, minuto e segundo) do termino da mesma.
'''

hora = float(input('Qual a hora de início:? '))
minutos = float(input('Qual a minuto de início:? '))
segundo = float(input('Qual a segundo de início:? '))
duração = float(input('Qual foi a duração em segundos? '))

hora_seg = hora * 3600
min_seg = minutos * 60

total_seg = hora_seg + min_seg + segundo + duração

total_hora = total_seg // 3600
total_min = (total_seg % 3600)
total_segundos = (total_seg % 3600) / 60 % 1
segundo = total_segundos * 60
total_min1 = ((total_seg % 3600) - segundo) / 60

print(f'{hora_seg},\n'
      f'{min_seg},\n'
      f'{segundo},\n'
      f'{duração},\n'
      f'{total_seg},\n'
      f'{total_hora},\n'
      f'{total_min},\n'
      f'{total_segundos},\n'
      f'{segundo}')

print(f'{total_hora:.0f}:{total_min1:.0f}:{segundo:.0f}')


'''
50 - Implemente um programa que cálcule o ano de nascimento de uma pessoa apartir de sua idade e do ano atual.
'''
idade = float(input('Quantos anos a pessoa tem? '))
ano = float(input('Qual é o ano atual? '))
ano_nasc = ano - idade
print(f'A pessoa nasceu no ano:{ano_nasc:.0f}')


'''
51 - Escreva um programa que leia as coordenadas x e y de pontos R² e calcule sua distância da origem (0, 0).
'''
x = float(input('Qual é a coordenada x? '))
y = float(input('Qual é a coordenada y? '))
d2 = x**2 + y**2
d = d2 * (1/2)
print(f'A distância da origem (0, 0) é = {d:.2f}')


'''
52 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada
deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do pêmio, e imprima
quento cada um ganharia do prêmio com base no valor investido.
'''
premio = float(input('Qual o valor do premio? R$ '))
jogador1 = float(input('Qual o valor investido pelo jogador nº 1? R$ '))
jogador2 = float(input('Qual o valor investido pelo jogador nº 2? R$ '))
jogador3 = float(input('Qual o valor investido pelo jogador nº 3? R$ '))
aposta = jogador1 + jogador2 + jogador3
premio_jogador1 = (jogador1 / aposta) * premio
premio_jogador2 = (jogador2 / aposta) * premio
premio_jogador3 = (jogador3 / aposta) * premio
print(f'O valor do premio do jogador nº 1 é = R$ {premio_jogador1:.2f}\n'
      f'O valor do premio do jogador nº 2 é = R$ {premio_jogador2:.2f}\n'
      f'O valor do premio do jogador nº 3 é = R$ {premio_jogador3:.2f}')


'''
53 - Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de
tela p. Imprima o custo para cercar este mesmo terreno com tela.
'''
c = float(input('Qual a comprimento do terreno? '))
l = float(input('Qual a largura do terreno? '))
p = float(input('Qual o preço do m² da tela? '))
terreno_m2 = c * l
custo_tela = p * terreno_m2
print(f'O terreno tem {terreno_m2:.0f}m² e terá um custo de R$ {custo_tela:.2f} para cercar este terreno.')
