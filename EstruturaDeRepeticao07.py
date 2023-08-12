numeros = []

for n in range(5):
    numero = int(input(f"Digite o número {n+1}: "))
    numeros.append(numero)


print(f"O maior número da lista {numeros} é", max(numeros))