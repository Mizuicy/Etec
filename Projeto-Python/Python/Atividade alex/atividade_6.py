#Atividade 6

vendedor = input('Digite o nome do vendedor: ')
salarioF = float(input('Digite o salario: '))
valorVenda = float(input('Digite o valor da Venda: '))

comissao = valorVenda * 0.15
salarioFinal = salarioF + comissao

print("Nome do {} \n"
    "Salário fixo: R$:{} \n"
    "Salário final com comissão: R$:{}".format(vendedor,salarioF,salarioFinal))
