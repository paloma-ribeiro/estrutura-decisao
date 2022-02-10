def calcula_folha_pagamento():
    valor_hora = float(input("Insira o valor da hora:"))
    horas_trabalhadas = float(input('Insira a quantidade de horas trabalhadas:'))
    salario_bruto = horas_trabalhadas * valor_hora

    if salario_bruto <= 900:
        salario_liquido = salario_bruto
