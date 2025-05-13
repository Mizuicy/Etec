i = 0
while i < 2:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    print("|(1)BAIXO|(2)MEDIO|(3)ALTO|")
    categoria_base = int(input("Digite a categoria base (1, 2 ou 3): "))  # Convertendo para int

    if 17 <= idade <= 20:
        categoria_final = categoria_base
    elif 21 <= idade <= 24:
        categoria_final = categoria_base + 1
    elif 25 <= idade <= 34:
        categoria_final = categoria_base + 2
    elif 35 <= idade <= 64:
        categoria_final = categoria_base + 3
    elif 65 <= idade <= 70:
        categoria_final = categoria_base + 4
    else:
        categoria_final = categoria_base + 5

    print(f"{nome}, categoria final: {categoria_final}")
    i += 1