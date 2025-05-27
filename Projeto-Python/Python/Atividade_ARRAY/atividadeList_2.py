nome = []

for x in range(10):
    nomes = (input(f"Digite o nome{x + 1}° = "))
    nome.append(nomes)
print("Os numeros da lista são")
for x, nome in enumerate(nome):
    print(f"{x + 1}°= {nome}")