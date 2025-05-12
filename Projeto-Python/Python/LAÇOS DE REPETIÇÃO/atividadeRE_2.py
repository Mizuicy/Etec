#atualização do codigo

TotalApto = 0
TotalInapto = 0

numberInt = int(input("Informe quantas pessoas você quer cadastrar: "))

for i in range(numberInt):

    nome = input("Informe seu nome =")
    idade = int(input("Informe sua idade ="))
    saude = input("Informe sua saude está boa (S)-Sim se não (N)-Não =")

    if idade >= 18 and saude.upper() == "S":
        print(f"Senhor(a){nome}, idade {idade}, e esta bem de saude tem todos os requisitos para servir")
        TotalApto += 1
    else:
        print(f"Senhor(a){nome},mas não tem idade suficiente {idade}")
        TotalInapto += 1


print(f"__Total de aptos: {TotalApto}")
print(f"__Total de inapto: {TotalInapto}")




