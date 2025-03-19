# Atividade 4

distancia = float(input('Digite a quantidade de Km: '))
gasolinaGasta = float(input('Digite a quantidade Gasolina: '))

totalGasto = distancia / gasolinaGasta

print("Fora {:.0f} Km {:.0f} gasto total {:.0f} por km".format(distancia, gasolinaGasta, totalGasto))
