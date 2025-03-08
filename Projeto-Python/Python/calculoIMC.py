nome = 'Adrian Smith'
altura = 1.50
peso = 65
imc = peso / altura ** 2

# f.strings  formatação de strings ou linhas 

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
