i = 0
while i < 5:
    
    A = int(input("Digite primeiro número: "))
    B = int(input("Digite segundo número: "))
    C = input("Digite um operador aritmetico (+, -, *, /): ")


    if C == "+":
        resultado = A + B
    elif C == "-":
        resultado = A - B
    elif C == "*":
        resultado = A * B
    elif C == "/":
        if B == 0:
            resultado = "Divisão por zero não é permitida."
        else:
            resultado = A / B
    else:
        resultado = "Operador inválido."

    i += 1
    print(f"Resultado: {resultado}")
    