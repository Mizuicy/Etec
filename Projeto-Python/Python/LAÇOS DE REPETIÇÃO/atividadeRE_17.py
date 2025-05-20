multiplo_de_5 = 0

for i in range(1, 11):

    valor = int(input(f"Digite o {i}º valor: "))
    if valor % 5 == 0:
        multiplo_de_5 += 1
    print("Entrada inválida. Digite um número inteiro.")
    continue

print(f"\nQuantidade de valores múltiplos de 5: {multiplo_de_5}")