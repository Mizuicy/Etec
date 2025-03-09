# condicao1 = False
# condicao2 = False
# condicao3 = False
# condicao4 = False

# if condicao1:
#     print('Este é o codigo do if')
# elif condicao2:
#     print('Condição 2')
# elif condicao3:
#     print('Condição 3')
# else:
#     print('Condição 4')

# primeiro_valor = input('Digite um valor: ')
# segundo_valor = input('Digite outro valor: ')

# if primeiro_valor >= segundo_valor:
#     print(f'o {primeiro_valor=} é maior que o  {segundo_valor=}' )
# else:
#     print(f'o {segundo_valor=} é maior que o  {primeiro_valor=}' )



# print(x > y)   # True  -> 10 é maior que 5
# print(x < y)   # False -> 10 não é menor que 5
# print(x >= y)  # True  -> 10 é maior ou igual a 5
# print(x <= y)  # False -> 10 não é menor ou igual a 5
# print(x == y)  # False -> 10 não é igual a 5
# print(x != y)  # True  -> 10 é diferente de 5

entrada = input('[E]ntrar [S]air:')
senha_digitada = input('Senha: ')

if entrada == 'E' and senha_digitada == '123456':
    print  ('Entrou') 
else:
    print('Erro ao entrar verificar ')