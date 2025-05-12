i = 0
while i < 10:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M)Masculino (F)Feminino: ")
    salario = 0,0
    
    if sexo.upper() == "M" and idade >= 30:
        salario = 100
    elif sexo.upper() == "M" and idade < 30:
        salario = 50
    elif sexo.upper() == "F" and idade >= 30:
        salario = 200
    elif sexo.upper() == "F" and idade < 30:
        salario = 80
    else:
        print("Sexo inválido")
        continue
    
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Sexo: {sexo}")
    print(f"Salario: R$:{salario}")
    i += 1
