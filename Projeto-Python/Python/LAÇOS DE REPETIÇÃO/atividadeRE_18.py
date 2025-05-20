for i in range(1, 6):
    print(f"\nTriângulo {i}")
    a = int(input("Digite o primeiro lado: "))
    b = int(input("Digite o segundo lado: "))
    c = int(input("Digite o terceiro lado: "))


    if a < b + c and b < a + c and c < a + b:
        print("É um triângulo!")
        if a == b == c:
            print("Tipo: Equilátero")
        elif a == b or b == c or a == c:
            print("Tipo: Isóscele")
        else:
            print("Tipo: Escaleno")
    else:
            print("Os valores não formam um triângulo.")
    print("Entrada inválida. Por favor, digite apenas números inteiros.")