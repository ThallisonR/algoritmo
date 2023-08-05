n1 = float(input("Informe sua nota 1: "))
n2 = float(input("Informe sua nota 2: "))
n3 = float(input("Informe sua nota 3: "))


media = (n1 + n2 + n3)/3

media_invalida = media < 0 or media > 10

aprovado = media >= 7
reprovado = media < 3

recuperacao = media > 3 and media < 7

if media_invalida:
    print(f"Média Inválida ->", {media})
elif aprovado:
    print(f'Parabéns! Você está APROVADO com média {media} \0/')
elif recuperacao:
    print(f'Quase! Você está RECUPERAÇÃO com média {media} !')
    n4 = float(input("Informe sua nota 4: "))
    media = (media + n4)/2
    aprovado = media>=5

    if aprovado:
        print(f'Parabéns! Você está APROVADO com média {media} \0/')
    else:
        print(f'Que pena! Você está REPROVADO com média {media} \0/')
elif reprovado:
    print(f'Que pena! Você está REPROVADO com média {media} \0/')