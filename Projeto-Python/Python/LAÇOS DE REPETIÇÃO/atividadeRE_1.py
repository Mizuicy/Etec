contador = int()


for numberInt in range(1, 9, 1):
    numberInt = int(input(f"Digite o {numberInt}° valor"))

    if numberInt >= 10 and numberInt <= 150:
        contador += 1

print(f"Essa quantidade {contador} está entre 10 e 150")
