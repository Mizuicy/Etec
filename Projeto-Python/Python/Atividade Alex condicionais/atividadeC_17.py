time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")

gols_time1 = int(input(f"Digite o número de gols de {time1}: "))
gols_time2 = int(input(f"Digite o número de gols de {time2}: "))

if gols_time1 > gols_time2:
    print(f"O vencedor é: {time1}")
elif gols_time2 > gols_time1:
    print(f"O vencedor é: {time2}")
else:
    print("EMPATE")