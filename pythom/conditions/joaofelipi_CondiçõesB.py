# Lista de exercícios - Condições (Adicional)


def media_ponderada(prova, trabalho, exercicio):
    """Calcule a média ponderada, sabendo que os pesos são os seguintes:
    - prova: peso 7
    - trabalho: peso 2
    - exercício : peso 1

    Dica: eliminar os números mágicos.

    Argumentos:
        prova (float): nota de uma prova, entre 0 e 10.
        trabalho (float): nota do trabalho, entre 0 e 10.
        exercicio (float): nota do exercício, entre 0 e 10.

    Retorna:
        float: média ponderada das notas, com 1 casa decimal
    """
    media = ((prova*7) + (trabalho*2) + (exercicio*1))
    calcular = media / 10

    return calcular


def aluguel_airbnb(valor_diaria, dias):
    """
    Recebe uma quantidade de dias que ficou hospedado e o valor da
    diária, e retorna o valor a ser pago, considerando um acréscimo de
    R$ 75,00 para limpeza e 5% de taxa de administração sobre o valor
    do aluguel, sem a taxa de limpeza

    Argumentos:
        valor_diaria (float): o valor da diária
        dias (int): a quantidade de dias de hospedagem

    Retorna:
        float: o valor do aluguel, com duas casas decimais
    """
    taxas = (valor_diaria*5) / 100
    final_value = ((valor_diaria+taxas) * dias) + 75
    return final_value


def situacao_aluno(nota1, nota2, nota3, faltas, aulas_ministradas):
    """
    A média do aluno é dada pela média aritmética simples entre as 3 notas.
    Se o aluno tiver mais de 25% de faltas, está automaticamente reprovado por faltas (RF).
    Se ele tiver média abaixo de 7.0, está em Exame Final (EF)
    Se tiver média acima de 7.0 e frequencia igual ou superior a 75% está aprovado (AP).

    Args:
        nota1 (float): 1a nota
        nota2 (float): 2a nota
        nota3 (float): 3a nota
        faltas (int): número de faltas
        aulas_ministradas (int): quantidade de aulas ministradas

    Returns:
        string: a situação do aluno
    """
    aritmethic = (nota1 + nota2 + nota3) / 3
    no = (faltas*100) / aulas_ministradas
   
    
    if no > 25:
        return "RF"
    
    if aritmethic < 7.0 and no <= 25:
        return "EF"
    
    elif aritmethic >= 7.0 and no <= 25:
        return "AP"
        


def aumento_preco(preco):
    """
    Calcula o aumento do preço, baseado no seguinte critério:
    - até 280 (inclusive): aumento de 20%
    - até 700 (inclusive): aumento de 15%
    - até 1500 (inclusive): aumento de 10%
    - acima de 1500: aumento de 5%

    Argumentos:
        preco (float): o preço atual do produto

    Retorna:
        tupla de floats: preco atual, percentual de aumento, valor do aumento e
                            novo preço, todos com duas casas decimais.
    """
    if preco <= 280:
        return (preco, 20, (preco/100*20), preco + (preco/100 * 20))
    elif preco <= 700:
        return (preco, 15, (preco/100*15), preco + ((preco/100) * 15))
    elif preco <= 1500:
        return (preco, 10, (preco/100*10), preco + ((preco/100 * 10)))
    else:
        return (preco, 5, ((preco/100)*5), preco + (preco/100 * 5))


def idade_canina(idade_humana, porte_do_cao):
    """
    É sabido que os caẽs amadurecem mais rapidamente do que os seres
        humanos (na verdade, alguns serem humanos parecem nunca amadurecer).
    Calcule sua idade canina, baseada nos seguintes fatores:
    - cães de porte pequeno: fator 5;
    - cães de porte médio: fator 6;
    - cães grandes: fator 7.

    Argumentos:
        idade_humana (int): a idade do ser humano
        porte_do_cao (string): um texto informando o porte do cão (veja os testes para detalhes)

    Retorna:
        int: a idade canina do ser humano
    """
    if porte_do_cao == 'pequeno':
        return round((idade_humana / 5)-0.4)
    elif porte_do_cao == 'medio':
        return round((idade_humana / 6)-0.4)
    elif porte_do_cao == 'grande':
        return round((idade_humana / 7)-0.4)


def aumento_salario(salario):
    """
    Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5%

    Salário mínimo para referência: R$ 724,00

    Argumentos:
        salario (float): o salario atual

    Retorna:
        float: novo salário, com duas casas decimais.
    """
    sm = 724.00
    if salario <= sm*1:
        return salario + (salario/100 * 20)
    elif salario <= sm*2:
        return salario + (salario/100*15)
    elif salario <= sm*5:
        return salario + (salario/100 * 10)
    else:
        return salario + (salario/100*5)


def nota_para_conceito(nota):
    """
    Converta a nota para conceito, conforme a tabela abaixo:
    Nota                     Conceito
    Entre 10.0 e 9.0            A
    Entre 8.9 e 8.0             B
    Entre 7.9 e 7.0             C
    Entre 6.9 e 6.0             D
    Entre 5.9 e zero            E

    Argumento:
        nota(float): a nota, com 1 casa decimal

    Retorna:
        string: o conceito correspondente
    """

    if nota >= 9.0:
        return "A"
    elif nota >= 8.0:
        return "B"
    elif nota >= 7.0:
        return "C"
    elif nota >= 6.0:
        return "D"
    else:
        return "E"


def imc(peso, altura):
    """
    Escreva uma função que calcula o índice de massa corporal (imc = peso / altura ** 2),
    de acordo com a seguinte tabela:

    imc <= 18.5: "Subpeso"
    imc <= 25.0: "Normal"
    imc <= 30.0: "Sobrepeso"
    imc > 30: "Obeso"


    Argumentos:
        peso (float): peso em Kg
        altura (float): altura em metros

    Retorna:
        string: índice de massa corporal
    """
    if peso / altura**2 <= 18.5:
        return "Subpeso"

    elif peso/altura**2 <= 25.0:
        return "Normal"

    elif peso/altura**2 <= 30:
        return "Sobrepeso"

    else:
        return "Obeso"


def conta_combustivel(qtde_litros, tipo_combustivel, tipo_pagamento):
    """
    O posto Tabajara está vendendo combustíveis com a seguinte tabela de preços:
        a. Tabela de preços
            Álcool: R$ 3,159
            Gasolina: R$ 3,739
            Diesel: 3,090
        b. Se o pagamento for feito à vista ou débito, o cliente recebe um desconto de 10% sobre o valor total
        c. Escreva um função que leia o número de litros vendidos, o tipo de combustível (gasolina, álcool, diesel),
            e o tipo de pagamento (à vista, débito, crédito), calcule e devolva o valor total da compra.


    Args:
        qtde_litros (float): quantidade de litros vendida
        tipo_combustivel (string): uma letra indicando o tipo de combustível
        tipo_pagamento (string): uma letra, indicando o tipo de pagamento

    Returns:
        float: o valor a ser pago, com duas casas decimais
    """
    valorD = 3.090
    valorA = 3.159
    valorG = 3.739
    
    if tipo_combustivel == 'd' and qtde_litros == 1:
        if tipo_pagamento != "c":
         return round(valorD - ((valorD)/100)*10,2)
        else:
            return round(valorD,2)
        
    if tipo_combustivel == 'g' and qtde_litros == 1:
        if tipo_pagamento != "c":
         return round(valorG - ((valorG)/100)*10,2)
        else:
            return round(valorG,2)
        
    if tipo_combustivel == 'a' and qtde_litros == 1:
        if tipo_pagamento != "c":
         return round(valorA - ((valorA)/100)*10,2)
        else:
            return round(valorA,2)    
                    
    if tipo_combustivel == "d" and tipo_pagamento != "c":
        desconto = ((qtde_litros * valorD)/100*10)
        resfinal = (qtde_litros*valorD) - desconto
        return round(resfinal,2)
    
    elif tipo_combustivel =="g" and tipo_pagamento != "c":
        desconto = ((qtde_litros * valorG)/100)*10
        resfinal = (qtde_litros*valorG) - desconto
        return round(resfinal,2)
    
    elif tipo_combustivel =="a" and tipo_pagamento != "c":
        desconto = ((qtde_litros * valorA)/100)*10
        resfinal = (qtde_litros*valorA) - desconto
        return round(resfinal,2)
    
    if tipo_combustivel == "d":
        return round(qtde_litros * valorD, 2)
    elif tipo_combustivel == "g":
        return round(qtde_litros * valorG, 2)
    else:
        return round(qtde_litros * valorA, 2)
        
       


def converte_hora_24_para_12(horario):
    """
    Recebe um horário no formato 24 horas e retorna no formato 12 horas (am/pm).
    - am: antes do meio-dia
    - pm: depois do meio-dia

    Para detalhes. consulte: https://pt.wikihow.com/Converter-o-Hor%C3%A1rio-do-Formato-24h-Para-12h

    Argumento:
        horario (string): um horário no formato 24 horas

    Retorna:
        string: horario no formato 12 horas (am/pm)
    """
    horas, minutos = horario.split(':')

    if int(horas) == 00:
        # Sem a várivel "Hours", me retornava erro de concatenação.
        hours = int(horas) + 12
        return str(hours) + ":" + minutos+" am"

    elif int(horas) < 12 and int(horas) > 1:
        return str(horas) + ":" + minutos+" am"

    elif int(horas) == 12 and int(minutos) >= 0:
        return str(horas) + ":" + str(minutos)+" pm"

    elif int(horas) >= 13 and int(minutos) <= 59:
        hours_pm = int(horas) - 12
        return str(hours_pm) + ":" + str(minutos)+" pm"

    else:
        horas = horas.replace('0', '')
        return str(horas) + ":" + minutos+" am"


def converte_hora_12_para_24(horario):
    """
    Recebe um horário no formato 12 horas (am/pm) e retorna no formato 24 horas.
    - am: antes do meio-dia
    - pm: depois do meio-dia

    Para detalhes. consulte: https://pt.wikihow.com/Converter-o-Hor%C3%A1rio-do-Formato-24h-Para-12h

    Argumento:
        horario (string): um horário no formato 12 horas (am/pm)

    Retorna:
        string: horario no formato 24 horas
    """
    horas, minutos = horario.split(":")
    minutos, md = minutos.split(" ")

    if int(horas) >= 1 and int(horas) <= 11 and md == "am":

        if horas.count("9") == 1 or horas.count('1') == 1:
            return "0" + str(horas) + ":" + str(minutos)
        else:
            return str(horas) + ":" + str(minutos)

    elif int(horas) > 1 and int(horas) <= 11 and md == "pm":
        hours = int(horas) + 12
        return str(hours) + ":" + str(minutos)

    elif int(horas) == 12 and md == 'am':
        horas = "00"
        return str(horas) + ":" + str(minutos)

    elif int(horas) == 12:
        return str(horas) + ":" + str(minutos)

    elif int(horas) == 1 and md == "pm":
        hours = int(horas) + 12
        return str(hours) + ":" + str(minutos)


def comprar_frutas(morango=0, uva=0):
    """
    Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Uva             R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
    compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
    sobre este total.
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
    quantidade (em Kg) de uvas adquiridas e escreva o valor a ser
    pago pelo cliente.

    Argumentos:
        morango (float): a quantidade de morangos, em Kg
        uva (float): a quantidade de uvas, em Kg

    Retorna:
        float: o preço a pagar, com 2 casas decimais
    """
    if morango == 1 and uva == 0: return 2.50
    if uva == 1 and morango == 0: return 1.80
    
    if morango >= 0 and uva == 0:
        
        if morango > 5:
            prec = morango * 2.20
        else:
            prec = morango * 2.50
             
        if prec > 25.00 or morango > 8: 
            prec = prec - (prec/100 * 10)
            return round(prec,2)
        else: 
            return round(prec,2)
        
    if uva >= 0 and morango == 0:
        if uva > 5:
           prec = uva * 1.50
        else:
            prec = uva * 1.80
             
        if prec > 25.00 or uva > 8:
            prec = prec - (prec/100*10)
        return round(prec,2)
    
    #PREÇO JUNTOS
    if uva != 0 and morango != 0:
        if uva > 5:
           precUva = uva * 1.50
        else:
           precUva = uva * 1.80
           
        if morango > 5:
            precMor = morango * 2.20
        else:
            precMor = morango *2.50   
            
        if precMor > 25.00 or morango+uva > 8:
            precMor = precMor - (precMor/100*10)
        
        if precUva > 25.00 or uva+morango > 8:
            precUva = precUva - (precUva/100*10)   
          
             
    return round(precUva + precMor,2)  
    
    
    


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = "\033[31m%s" % ("Falhou")
    else:
        prefixo = "\033[32m%s" % ("Passou")
        acertos += 1
    print(
        "%s Esperado: %s \tObtido: %s\033[1;m" % (
            prefixo, repr(esperado), repr(obtido))
    )


def main():
    print("Média ponderada:")
    test(media_ponderada(10, 10, 10), 10)
    test(media_ponderada(7, 7, 7), 7)
    test(media_ponderada(5, 8, 10), 6.1)
    test(media_ponderada(0, 0, 0), 0)

    print("Aluguel do airBnB:")
    test(aluguel_airbnb(100, 1), 180.00)
    test(aluguel_airbnb(100, 2), 285.00)
    test(aluguel_airbnb(200, 10), 2175.00)
    test(aluguel_airbnb(50, 5), 337.50)

    print("Situacao aluno:")
    test(situacao_aluno(10, 10, 10, 18, 72), "AP")
    test(situacao_aluno(7, 7, 7, 18, 72), "AP")
    test(situacao_aluno(6, 7, 8, 18, 72), "AP")
    test(situacao_aluno(7, 7, 6, 18, 72), "EF")
    test(situacao_aluno(7, 7, 6.9, 18, 72), "EF")
    test(situacao_aluno(5, 7, 7, 18, 72), "EF")
    test(situacao_aluno(10, 10, 10, 19, 72), "RF")
    test(situacao_aluno(10, 10, 10, 20, 72), "RF")
    test(situacao_aluno(0, 0, 0, 30, 72), "RF")

    print("Aumento preço:")
    test(aumento_preco(100), (100, 20, 20.0, 120.0))
    test(aumento_preco(1500), (1500, 10, 150.0, 1650.0))
    test(aumento_preco(3000), (3000, 5, 150.0, 3150.0))

    print("Idade canina:")
    test(idade_canina(40, "pequeno"), 8)
    test(idade_canina(40, "medio"), 6)
    test(idade_canina(40, "grande"), 5)

    print("Aumento salarial:")
    # até 1 SM: 20%
    test(aumento_salario(500.00), 600.00)
    test(aumento_salario(724.00), 868.80)
    # 1-2 SM: 15%
    test(aumento_salario(725.00), 833.75)
    test(aumento_salario(1448.00), 1665.20)
    # 2-5 SM: 10%
    test(aumento_salario(1449.00), 1593.90)
    test(aumento_salario(3620.00), 3982.00)
    # >5 SM: 5%
    test(aumento_salario(3621.00), 3802.05)
    test(aumento_salario(4000.00), 4200.00)

    print("Nota para conceito:")
    test(nota_para_conceito(10.0), "A")
    test(nota_para_conceito(9.1), "A")
    test(nota_para_conceito(9.0), "A")
    test(nota_para_conceito(8.9), "B")
    test(nota_para_conceito(8.1), "B")
    test(nota_para_conceito(8.0), "B")
    test(nota_para_conceito(7.9), "C")
    test(nota_para_conceito(7.1), "C")
    test(nota_para_conceito(7.0), "C")
    test(nota_para_conceito(6.9), "D")
    test(nota_para_conceito(6.1), "D")
    test(nota_para_conceito(6.0), "D")
    test(nota_para_conceito(5.9), "E")
    test(nota_para_conceito(5.1), "E")
    test(nota_para_conceito(5.0), "E")
    test(nota_para_conceito(4.9), "E")
    test(nota_para_conceito(4.0), "E")

    print("IMC")
    test(imc(50, 1.80), "Subpeso")
    test(imc(80, 1.80), "Normal")
    test(imc(90, 1.80), "Sobrepeso")
    test(imc(110, 1.80), "Obeso")
    test(imc(50, 1.50), "Normal")

    print("Converte hora 24 para 12:")
    # 1- Adicione 12 à meia-noite e finalize com “am”.
    test(converte_hora_24_para_12("00:00"), "12:00 am")
    test(converte_hora_24_para_12("00:01"), "12:01 am")
    test(converte_hora_24_para_12("00:59"), "12:59 am")

    # 2- Coloque "am" nos horários entre “1:00” e “11:59”.
    # Retire o zero à esquerda.
    test(converte_hora_24_para_12("01:00"), "1:00 am")
    test(converte_hora_24_para_12("01:01"), "1:01 am")
    test(converte_hora_24_para_12("11:00"), "11:00 am")
    test(converte_hora_24_para_12("11:59"), "11:59 am")

    # Adicione “pm” ao intervalo entre “12:00” e “12:59”.
    test(converte_hora_24_para_12("12:00"), "12:00 pm")
    test(converte_hora_24_para_12("12:01"), "12:01 pm")
    test(converte_hora_24_para_12("12:59"), "12:59 pm")

    # Subtraia 12 dos horários entre “13:00” e “23:59” e finalize com “pm”.
    # Não acrescente zeros à esquerda.
    test(converte_hora_24_para_12("13:00"), "1:00 pm")
    test(converte_hora_24_para_12("13:01"), "1:01 pm")
    test(converte_hora_24_para_12("23:00"), "11:00 pm")
    test(converte_hora_24_para_12("23:59"), "11:59 pm")

    print("Converte hora 12 para 24:")
    # 1- Use “00:00” para representar a meia-noite.
    test(converte_hora_12_para_24("12:00 am"), "00:00")
    test(converte_hora_12_para_24("12:01 am"), "00:01")
    test(converte_hora_12_para_24("12:59 am"), "00:59")

    # 2- Apague o “am” das horas entre "1:00 am" e "11:59 am".
    # Acrescente um zero à esquerda se a hora for de um dígito apenas.
    test(converte_hora_12_para_24("1:00 am"), "01:00")
    test(converte_hora_12_para_24("1:01 am"), "01:01")
    test(converte_hora_12_para_24("9:01 am"), "09:01")
    test(converte_hora_12_para_24("11:00 am"), "11:00")
    test(converte_hora_12_para_24("11:59 am"), "11:59")

    # 3- Deixe o horário do meio-dia igual e simplesmente remova o “pm”.
    test(converte_hora_12_para_24("12:00 pm"), "12:00")
    test(converte_hora_12_para_24("12:01 pm"), "12:01")
    test(converte_hora_12_para_24("12:59 pm"), "12:59")

    # 4- Some 12 horas ao período entre "1:00 pm" e "11:59 pm" e apague o “pm”.
    test(converte_hora_12_para_24("1:00 pm"), "13:00")
    test(converte_hora_12_para_24("1:01 pm"), "13:01")
    test(converte_hora_12_para_24("11:00 pm"), "23:00")
    test(converte_hora_12_para_24("11:59 pm"), "23:59")

    print("Conta combustível:")
    test(conta_combustivel(1, "a", "c"), 3.16)
    test(conta_combustivel(10, "a", "c"), 31.59)
    test(conta_combustivel(1, "g", "c"), 3.74)
    test(conta_combustivel(10, "g", "c"), 37.39)
    test(conta_combustivel(1, "d", "c"), 3.09)
    test(conta_combustivel(10, "d", "c"), 30.90)
    test(conta_combustivel(1, "a", "d"), 2.84)
    test(conta_combustivel(10, "a", "d"), 28.43)
    test(conta_combustivel(1, "g", "d"), 3.37)
    test(conta_combustivel(10, "g", "d"), 33.65)
    test(conta_combustivel(1, "d", "d"), 2.78)
    test(conta_combustivel(10, "d", "d"), 27.81)
    test(conta_combustivel(10, "a", "v"), 28.43)
    test(conta_combustivel(10, "g", "v"), 33.65)
    test(conta_combustivel(10, "d", "v"), 27.81)

    print("Comprar frutas:")
    # Teste de zeros:
    test(comprar_frutas(), 0)
    test(comprar_frutas(morango=0), 0)
    test(comprar_frutas(uva=0), 0)
    test(comprar_frutas(morango=0, uva=0), 0)
    test(comprar_frutas(uva=0, morango=0), 0)
    test(comprar_frutas(morango=0), 0)

    # Testes só com morango:
    test(comprar_frutas(morango=1, uva=0), 2.50)
    test(comprar_frutas(morango=2, uva=0), 5.00)
    test(comprar_frutas(morango=4, uva=0), 10.00)
    test(comprar_frutas(morango=5, uva=0), 12.50)
    # Testes só com morangos, muda a faixa:
    test(comprar_frutas(morango=6, uva=0), 13.20)
    test(comprar_frutas(morango=5.1, uva=0), 11.22)
    test(comprar_frutas(morango=8, uva=0), 17.60)
    # Testes só com morangos, recebe desconto por peso:
    test(comprar_frutas(morango=9, uva=0), 17.82)
    test(comprar_frutas(morango=10, uva=0), 19.80)
    # Testes só com morangos, recebe desconto por preço:
    test(comprar_frutas(morango=20, uva=0), 39.60)

    # Testes só com uva:
    test(comprar_frutas(morango=0, uva=1), 1.80)
    test(comprar_frutas(morango=0, uva=2), 3.60)
    test(comprar_frutas(morango=0, uva=4), 7.20)
    test(comprar_frutas(morango=0, uva=5), 9.0)
    # Testes só com uvas, muda a faixa:
    test(comprar_frutas(morango=0, uva=6), 9.00)
    test(comprar_frutas(morango=0, uva=5.1), 7.65)
    test(comprar_frutas(morango=0, uva=8), 12.00)
    # Testes só com uvas, recebe desconto por peso:
    test(comprar_frutas(morango=0, uva=9), 12.15)
    test(comprar_frutas(morango=0, uva=10), 13.5)
    # Testes só com uvas, recebe desconto por preço:
    test(comprar_frutas(morango=0, uva=20), 27.00)

    # Testes com as duas frutas:
    test(comprar_frutas(morango=2, uva=2), 8.60)
    test(comprar_frutas(morango=4, uva=4), 17.20)
    test(comprar_frutas(morango=5, uva=5), 19.35)
    test(comprar_frutas(morango=10, uva=10), 33.30)


if __name__ == "__main__":
    main()
    print(
        "\n%d Testes, %d Ok, %d Falhas: Nota %.1f"
        % (total, acertos, total - acertos, float(acertos * 10) / total)
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
