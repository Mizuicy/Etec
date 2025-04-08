valor_venda = float(input("Digite o valor da venda: R$ "))

print("Escolha a condição de pagamento:")
print("1 - Venda à Vista - Desconto de 10%")
print("2 - Venda a Prazo 30 dias - Desconto de 5%")
print("3 - Venda a Prazo 60 dias - Mesmo preço")
print("4 - Venda a Prazo 90 dias - Acréscimo de 5%")
print("5 - Venda com Cartão de Débito - Desconto de 8%")
print("6 - Venda com Cartão de Crédito - Desconto de 7%")

escolha = int(input("Digite o número da condição de pagamento: "))


if escolha == 1:
    valor_final = valor_venda * 0.90
elif escolha == 2:
    valor_final = valor_venda * 0.95
elif escolha == 3:
    valor_final = valor_venda
elif escolha == 4:
    valor_final = valor_venda * 1.05
elif escolha == 5:
    valor_final = valor_venda * 0.92
elif escolha == 6:
    valor_final = valor_venda * 0.93
else:
    print("Opção inválida.")

print(f"O valor final da compra é: R$ {valor_final:.2f}")
