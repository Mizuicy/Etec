total_reajuste = 0
i = 0
salarioMinimo = 1518.00
reajuste = float

while i in range(3):
    print(f"\nFuncionário {i + 1}°")
    nome = input("Digite seu nome: ")
    salarioFuncionario = int(input("Quantos salario minimos vc recebe:"))

    salarioMinimo = salarioFuncionario / salarioMinimo
    
    if salarioMinimo <= 3:
        reajuste = salarioFuncionario * 0.50
        i += 1
    elif  salarioMinimo <= 10:
        reajuste = salarioFuncionario * 0.2
        i += 1
    elif salarioMinimo <= 20:
        reajuste = salarioFuncionario * 0.15
        i += 1
    else:
        reajuste = salarioFuncionario * 0.10
        i += 1
        

    salarioFinal = salarioFuncionario + reajuste
    total_reajuste += reajuste
    print(f"__O SENHOR(A){nome} vai receber um aumento de R$:{reajuste} no salario esté mês__")
    print(f"__O SEU NOVO SALARIO É DE {salarioFinal}__")


print(f"Total de aumento na folha foi de R$ {total_reajuste}")
