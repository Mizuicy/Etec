i = 0
limite_Inicial = int(input("Digite o limite inicial: "))
limite_Maximo = int(input("Digite o limite máximo: "))

for i in range(limite_Inicial, limite_Maximo, 1):
    if i % 2 == 0:
        print(f" {i}° Número par")
    elif i % 2 == 1:
        print(f" {i}° Número ímpar")
print("Fim do programa")