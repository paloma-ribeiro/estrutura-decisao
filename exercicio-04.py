def verifica_letra(letra):
    vogal = ('a', 'e', 'i', 'o', 'u')
    if letra in vogal:
        print('Vogal')
    else:
        print('Consoante')


verifica_letra('a')
verifica_letra('j')
verifica_letra('e')
verifica_letra('i')
verifica_letra('o')
verifica_letra('u')
verifica_letra('p')
verifica_letra('w')