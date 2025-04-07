nome =  str(input("Digite o seu nome "))
nota_1 = float(input("Digite a nota "))
nota_2 = float(input("Digite a nota "))
nota_3 = float(input("Digite a nota "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print(f"{nome} foi aprovado com media = {media}")
    print(f"Parabens {nome}")
elif media <= 5:
    print(f"Aluno {nome} foi reprovado com media = {media} ")
elif media >= 5.1 or media <= 6.9:
    print(f"Aluno {nome} ficou de recuperação com media = {media}")