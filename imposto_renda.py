

def inss(salario):

    salario = float(input("Informe o valor do salário: "))

    faixa1 = salario <= 1320
    faixa2 = salario > 1320 and salario <= 2571.29
    faixa3 = salario > 2571.29 and salario <= 3856.94
    faixa4 = salario > 3856.94 and salario <= 7507.49

    if faixa1:
        salario * 0.075
    elif faixa2:
        return (salario - 1320) * 0.09 + 99
    elif faixa3:
        return (salario - 2571.30) * 0.12 + 211.61
    elif faixa4:
       return (salario - 3856.95) * 0.14 + 365.89
    
    return 876.97

salario = float(input("Digite o valor do salário: "))


print(inss(salario))