"""
Documentando funções com docstrings

# OBS: Podemos ter acesso á documentação de uma função em Python utilizando a propriedade especial __doc__

# Exemplos:

def diz_oi():
    #'''Uma função simples que retorna a string 'Oi!''' # AS ASPAS SÃO DUPLAS E NÃO SIMPLES SÓ FOI USADO DEVIDO ESTAR
                                                        # EM COMENTÁRIO PARA NÃO GERAR ERRO
    return 'Oi! '

print(diz_oi.__doc__)
# Retorno / Saída:
# Uma função simples que retorna a string 'Oi!'


def diz_oi():
    '''Uma função simples que retorna a string 'Oi!''' # AS ASPAS SÃO DUPLAS E NÃO SIMPLES SÓ FOI USADO DEVIDO ESTAR
                                                        # EM COMENTÁRIO PARA NÃO GERAR ERRO
    return 'Oi! '

print(diz_oi.__doc__)

# Retorno / Saída:
# Uma função simples que retorna a string 'Oi!'

def exponencial(numero, potencia=2):
    '''                                                 # AS ASPAS SÃO DUPLAS E NÃO SIMPLES SÓ FOI USADO DEVIDO ESTAR
                                                        # EM COMENTÁRIO PARA NÃO GERAR ERRO

    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'portencia'.
    '''
    return numero ** potencia


# Podemos ainda fazer acesso á documentação com a função help()

"""


















