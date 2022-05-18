"""
Estruturas condicionais
if (Se), else (Senão), elif (Senão Se)


"""
"""
# Exemplo de estrutura condicional em C
idade = 26
if(idade < 18) {
    print("Menor de idade");
}else if(idade == 18){
    print("Tem 18 anos");
}else{
    print("É menor de idade")
}
"""
"""
# Exemplo de estrutura condicional em Java
idade = 18
if(idade < 18) {
    System.out.println("Menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos");
}else{
    System.out.println("Maior de idade");
}
"""
idade = 26

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')

"""
# Não aconselhavel mas pode ser feito conforme abaixo ou seja separando a estrutura condicional
if idade < 18:
    print('Menor de idade')

if idade == 18:
    print('Tem 18 anos')

if idade == 26:
    print('Tem 26 anos')

elif idade > 18:
    print('Maior de idade')
"""