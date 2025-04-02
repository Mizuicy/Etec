# Atividade 2

A = int(input('digite o numero A:'))
B = int(input('digite o numero B:'))
if A < B:
    print('Valor de A é menor do que valor de B.')
else:
    C = A
    A = B
    B = C
    print(f'A = {A} e B {B}')
