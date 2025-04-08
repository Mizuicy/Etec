idade = int(input("Digite a idade "))
nome = input("Digite seu nome ")

if idade >= 5:
    print(f"{nome} está na categoria:")
    print("Infantil")
elif idade >= 11:
    print(f"{nome} está na categoria:")
    print("Juvenil")
elif idade >= 16 :
    print(f"{nome} está na categoria:")
    print("Junior")
elif idade >= 21:
    print(f"{nome} está na categoria:")
    print("Profissional")
else:
    print(f"{nome} O senhor passou da idade para ser jogador")