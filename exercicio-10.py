def saudacao():
    turno = input('Informe o turno que você estuda: M-Matutino, V-Vespertino, N-Noturno: ')
    if turno == 'M-Matutino' or turno.upper() == 'M':
        return 'Bom Dia!'
    if turno == 'V-Vespertino' or turno.upper() == 'V':
        return 'Boa Tarde!'
    if turno == 'N-Noturno' or turno.upper() == 'N':
        return 'Boa Noite!'
    return 'Valor Inválido!'


print(saudacao())
