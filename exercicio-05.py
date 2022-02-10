def calcula_media(nota1, nota2):
    notas = (nota1, nota2)
    media = sum(notas) / len(notas)
    if 7 <= media < 10:
        return print('Aprovado')
    if media < 7:
        return print('Reprovado')
    elif media == 10:
        return print('Aprovado com Distinção')


calcula_media(5, 3)
calcula_media(8, 7)
calcula_media(10, 10)
