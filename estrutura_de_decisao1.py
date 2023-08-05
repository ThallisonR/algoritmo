# Verifica se a letra digitada é vogal

vogais = ("a", "e", "i", "o", "u")

letra = input("Digite uma letra do alfabeto:\n")

eh_vogal = letra.lower() in vogais

if eh_vogal:
    print("VOGAL")
else:
    print("NÃO VOGAL")