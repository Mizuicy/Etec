# salario = float(input("Digite o valor do seu Salario"))
#
# if salario <= 2000:
#     print("Isento")
#
# elif salario >= 2000.01 and salario <= 5000.00:
#     percentual = salario * 100 / 0.10
#     print("Valor de 10% de Imposto sobre o salario")
#
# elif salario > 5000.00:
#     percentual = salario * 0.2
#     print("Valor de 20% de Imposto sobre o salario")
# else:
#     print("Erro 404")

# camisaQuantidadePequena = int(input("Qual a quantidade de camisa Pequena"))
# camisaQuantidadeMedia = int(input("Qual a quantidade de camisa Media"))
# camisaQuantidadeGrande = int(input("Qual a quantidade de camisa Grande"))
#
# camisaPequena = camisaQuantidadePequena * 63
# camisaMedia = camisaQuantidadeMedia * 71
# camisaGrande = camisaQuantidadeGrande * 87
#
# total = camisaPequena + camisaMedia + camisaGrande
#
# print(f"Valor total arrecadado é de {total} ")

nome = input("Seu nome")
print("Como é o meio de trabalho")
localTrabalho = input("Interno(I) ou Externo(E)")

print("Qual seu cargo ? ")
cargo = input("Diretor=(D), Gerente=(G) Lider=(L)")

valorSalario = float(input("Qual o valor salarial"))


if localTrabalho == "I" and cargo == "D":
    total = valorSalario * 0.10 + 1000
    print(nome)
    print("Diretor")
    print("Externo")
    print(f"Salario é {total}")
elif localTrabalho == "I" and cargo == "G":
    total = (valorSalario * 0.10) + 500
    print(nome)
    print("Gerente")
    print("Externo")
    print(f"Salario é {total}")
elif localTrabalho == "I" and cargo == "L":
    total = (valorSalario * 0.10) + 200
    print(nome)
    print("Lider")
    print("Externo")
    print(f"Salario é {total}")
else:
    if localTrabalho == "E" and cargo == "D":
        total = (valorSalario * 0.20) + 1000
        print(nome)
        print("Diretor")
        print("Externo")
        print(f"Salario é {total}")
    elif localTrabalho == "E" and cargo == "G":
        total = (valorSalario * 0.20) + 500
        print(nome)
        print("Gerente")
        print("Externo")
        print(f"Salario é {total}")
    elif localTrabalho == "E" and cargo == "L":
        total = (valorSalario * 0.20) + 200
        print(nome)
        print("Lider")
        print("Externo")
        print(f"Salario é {total}")
    else:
        print("Erro 404")


