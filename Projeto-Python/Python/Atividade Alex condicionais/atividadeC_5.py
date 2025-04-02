# ATIVIDADE 5

salario = float(input("Digite o valor do seu Salario"))
salarioFinal = float
percentual = float

if salario <= 600:
    percentual = salario * 0.30
    salarioFinal = salario + percentual
    print(salarioFinal)
    
elif salario >= 600.01 and salario <= 1100.00 :
    percentual = salario * 0.25
    salarioFinal = salario + percentual
    print(salarioFinal)
    
elif salario >= 1100.01 and salario <= 2400.00 :
    percentual = salario * 0.20
    salarioFinal = salario + percentual
    print(salarioFinal)
    
elif salario >= 2400.01 and salario <= 3550.00 :
    percentual = salario * 0.15
    salarioFinal = salario + percentual
    print(salarioFinal)
    
elif salario >= 3550.00:
    percentual = salario * 0.10
    salarioFinal = salario + percentual
    print(salarioFinal)
else:
    print("Invalido")