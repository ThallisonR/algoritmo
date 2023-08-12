# A função tem que ser especialista em algo:

def bem_vindo():
    print("Bem vindo!")

def entrada(texto):
    return int(input(texto))

def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

####################################

# Crie uma função que retorne o valor do imposto de previdência atual de um salário

n1 = entrada("Digite um número: ")
n2 = entrada("Digite outro número: ")

resultado = somar(n1,n2)

print(resultado)

#################################################################################

# Crie uma função que retorne o valor do imposto de previdência atual de um salário

def imposto_renda():
    salario = float(input("Informe o valor do salário: "))
    aliquota = 0
    if salario <= 1320:

    
        aliquota = (7.5)/100
    if salario >= 1320.01 and salario <  2571.29:
        aliquota = (9)/100
    if salario >= 2571.30 and salario <   3856.94:
        aliquota = (12)/100
    if salario >= 3856.95 and salario <    7507.49:
        aliquota = (14)/100

    dedução = salario * aliquota

    imposto = salario-dedução
    print(imposto)
    return imposto

imposto_renda()