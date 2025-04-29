for numberInt in range(0, 8, 1):

    nome = input("Informe seu nome")
    idade = int(input("Informe sua idade"))
    saude = input("Informe sua saude está boa (S)-Sim se não (N)-Não ")

if idade >= 18:
    if saude.upper() == "S":
        print(f"Senhor(a){nome}, idade {idade}, e esta bem de saude tem todos os requisitos para servir")
    else:
        print(f"Senhor(a){nome}, idade {idade},mas não está bem de saude")
else:
    print(f"Senhor(a){nome},mas não tem idade suficiente {idade}")




