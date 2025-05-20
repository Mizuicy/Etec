for i in range(1, 31):
    print(f"\nPessoa {i}")

    tipo = int(input("Digite o tipo de cliente (1-Residência, 2-Comércio, 3-Indústria): "))
    consumo = float(input("Digite o consumo em kWh: "))

    if tipo == 1:
        valor_kw = 0.60
    elif tipo == 2:
        valor_kw = 0.48
    elif tipo == 3:
        valor_kw = 1.29
    else:
        print("Tipo de cliente inválido. Pulando para a próxima pessoa.")
        continue

    total = consumo * valor_kw
    print(f"Valor da conta de luz: R$ {total:.2f}")