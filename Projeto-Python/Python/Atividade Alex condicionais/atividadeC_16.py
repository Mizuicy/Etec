a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a < b and a < c:
    if b < c:
        print(f"Os valores em ordem crescente são: {a}, {b}, {c}")
    else:
        print(f"Os valores em ordem crescente são: {a}, {c}, {b}")
elif b < a and b < c:
    if a < c:
        print(f"Os valores em ordem crescente são: {b}, {a}, {c}")
    else:
        print(f"Os valores em ordem crescente são: {b}, {c}, {a}")
else:
    if a < b:
        print(f"Os valores em ordem crescente são: {c}, {a}, {b}")
    else:
        print(f"Os valores em ordem crescente são: {c}, {b}, {a}")