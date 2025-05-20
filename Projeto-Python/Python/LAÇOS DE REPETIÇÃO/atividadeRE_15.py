for i in range(1, 51):
    print(f"Professor {i}")
    
    nivel = int(input("Digite o nível do professor (1, 2 ou 3): "))
    horas = float(input("Digite o número de horas/aula: "))

    if nivel == 1:
        salario = horas * 12.00
    elif nivel == 2:
        salario = horas * 17.00
    elif nivel == 3:
        salario = horas * 25.00
    else:
        print("Nível inválido. Pulando para o próximo professor.\n")
        continue

    print(f"Salário do professor: R$ {salario:.2f}\n")