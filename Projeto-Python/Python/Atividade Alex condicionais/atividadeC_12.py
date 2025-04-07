idade = int(input("Digite a idade "))
nome = input("Digite seu nome ")

if idade >= 5 and idade <= 10:
    print(f"{nome} está na categoria:")
    print("Infantil")
elif idade >= 11 and idade <= 15:
    print(f"{nome} está na categoria:")
    print("Juvenil")
elif idade >= 16 and idade <= 20:
    print(f"{nome} está na categoria:")
    print("Junior")
elif idade >= 21 and idade <= 25:
    print(f"{nome} está na categoria:")
    print("Profissional")
else:
    print(f"{nome} O senhor passou da idade para ser jogador")