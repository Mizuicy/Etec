# Atividade 2

# A = int(input('digite o numero A:'))
# B = int(input('digite o numero B:'))
# if A < B:
# print('Valor de A é menor do que valor de B.')
# else:
# C = A
# A = B
# B = C
# print(f'A = {A} e B {B}')

# Atividade 3

# senha = input('Informe sua senha: ')
# senha_correta = "40028922"
# if senha == senha_correta:
# print('Acesso permitido.')
# else
# print('Você não tem acesso ao sistema.')

# Atividade 4

# dia = int(input('Que dia é hj?'))
# if (dia == 1):
#     print('Hoje é Segunda - Feira ')
# else:
#     if (dia == 2):
#         print('Hoje é Terça - Feira ')
#     else:
#         if (dia == 3):
#             print('Hoje é Quarta - Feira ')
#         else:
#             if (dia == 4):
#                 print('Hoje é Quinta - Feira ')
#             else:
#                 if (dia == 5):
#                     print('Hoje é Sexta - Feira ')
#                 else:
#                     if (dia == 6):
#                         print('Hoje é Sábado ')
#                     else:
#                         if (dia == 7):
#                             print('Hoje é Domingo ')
#                         else:
#                             print('valor invalido')
                            
# ATIVIDADE 5

salario = float(input("Digite o valor do seu Salario"))
salarioFinal = int
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
