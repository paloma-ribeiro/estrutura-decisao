def reajuste_salario(salario):
    if salario <= 280:
        percentual = 0.2
        valor_aumento = salario * percentual
        novo_salario = salario + valor_aumento

    elif salario < 700:
        percentual = 0.15
        valor_aumento = salario * percentual
        novo_salario = salario + valor_aumento

    elif salario < 1500:
        percentual = 0.1
        valor_aumento = salario * percentual
        novo_salario = salario + valor_aumento

    else:
        percentual = 0.05
        valor_aumento = salario * percentual
        novo_salario = salario + valor_aumento

    print('Salário antes do reajuste:', salario)
    print('Percentual de aumento aplicado:', percentual)
    print('Valor do aumento:', valor_aumento)
    print('Novo salário, após o aumento:', novo_salario)


reajuste_salario(280)
reajuste_salario(600)
reajuste_salario(800)
reajuste_salario(1600)
reajuste_salario(700)
reajuste_salario(1500)
reajuste_salario(1501)
