a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a > b  and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("erro")
