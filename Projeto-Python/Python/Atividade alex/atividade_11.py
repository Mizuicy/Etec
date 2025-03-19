#Atividade 11

fabricaçao = float(input('Valor da fabricação:'))
maodeObra = float(input('Valor da mão de obra:'))

valorVenda = fabricaçao + (fabricaçao * (maodeObra / 100))

print("Valor da Venda = R${:.1f}".format(valorVenda))