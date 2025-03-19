#Atividade 10

compra = float(input('Valor da compra:'))
parcela = float(input('Enquantas Parcelas:'))

valorDaParcela = compra / parcela

print("Valor das parcelas = R${:.2f}".format(valorDaParcela))