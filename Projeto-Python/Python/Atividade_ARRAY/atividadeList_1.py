numero = []

for x in range(10):
    numeros = (int(input(f"Digite o {x + 1} = ")))
    numero.append(numeros)
print("Os numeros da lista são")
for x, numero in enumerate(numero):
    print(f"{x + 1}°= {numeros}")