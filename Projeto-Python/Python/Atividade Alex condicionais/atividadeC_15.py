a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a > b and a > c:
    soma = a + max(b, c)
elif b > a and b > c:
    soma = b + max(a, c)
else:
    soma = c + max(a, b)

print(f"A soma dos dois maiores valores é: {soma}")