#Atividade 8

a = float(input('Digite valor de A: '))
b = float(input('Digite valor de B: '))

c = a
a = b
b = c

print("Valor de A={:.0f} \nValor de B={:.0f}".format(a, b))