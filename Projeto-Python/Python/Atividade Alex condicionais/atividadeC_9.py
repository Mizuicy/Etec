numero_1 = int(input("Digite o primeiro numero "))

if numero_1 >= 100 and numero_1 <= 200:
    print(f" O numero {numero_1}  está entre 100 e 200")
elif numero_1 <= 99:
    print(f"O numero está abaixo de 100 ")
elif numero_1 >= 201:
    print(f"O numero está acima de 200 ")
else:
    print("Erro")