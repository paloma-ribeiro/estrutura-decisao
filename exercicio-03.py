def verifica_sexo(letra):
    if letra.upper() == 'F':
        return print('F - Feminino')
    if letra.upper() == 'M':
        return print('M - Masculino')
    return print('Sexo Inválido')


verifica_sexo('F')
verifica_sexo('f')
verifica_sexo('M')
verifica_sexo('m')
verifica_sexo('B')
verifica_sexo('b')
