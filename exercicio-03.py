def verifica_sexo(letra):
    if letra.upper() == 'F':
        print('F - Feminino')
    elif letra.upper() == 'M':
        print('M - Masculino')
    else:
        print('Sexo Inválido')


verifica_sexo('F')
verifica_sexo('f')
verifica_sexo('M')
verifica_sexo('m')
verifica_sexo('B')
verifica_sexo('b')
