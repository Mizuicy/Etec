carros_2000 = 0
carros_2001 = 0


while True:
    valorCarro = float(input("Digite o valor do carro: "))
    anoCarro = int(input("Digite o ano do carro: "))
    valorPaga = float
    if anoCarro <= 2000:
        descontoCarro = valorCarro * 0.12
        carros_2000 += 1
    elif anoCarro > 2000:
        descontoCarro = valorCarro * 0.07
        carros_2001 += 1
    else:
        print("Ano inválido")
        continue
    
    valorCarro -= descontoCarro
    print(f"Desconto de: {descontoCarro}")
    print(f"Valor do carro com desconto: {valorCarro}")
    
    resposta = input("Deseja continuar calculando (S/N)")
    if resposta.upper() == "N":
        print(f"Total de carros 2000: {carros_2000}")
        print(f"Total de carros 2001: {carros_2001}")
        print(f"Total de carros que saiu: {carros_2000 + carros_2001}")
        break
