print("Produto em lista; \n" +
    "X-Salada com coca-cola ID = 100 \n" +
    "Hot dog com suco de laranja ID = 200 \n" +
    "Sanduiche natural com suco de uva ID = 300 \n" +
    "Misto Quente com fanta laranja ID = 400\n"+
    "Pão com manteiga com café ID = 500\n"+
    "Pão com manteiga na chapa com café com leite ID = 600\n")

codigoProduto = int(input("Qual vai ser seu pedido "))

if codigoProduto == 100:
    print("Pedido = X-Salada com coca-cola")
elif codigoProduto == 200:
    print("Pedido = Hot dog com suco de laranja")
elif codigoProduto == 300:
    print("Sanduiche natural com suco de uva")
elif codigoProduto == 400:
    print("Pedido = Misto Quente com fanta laranja")
elif codigoProduto == 500:
    print("Pedido = Pão com manteiga com café")
elif codigoProduto == 600:
    print("Pedido = Pão com manteiga na chapa com café com leite")
else:
    print("Código informado inválido")
    


