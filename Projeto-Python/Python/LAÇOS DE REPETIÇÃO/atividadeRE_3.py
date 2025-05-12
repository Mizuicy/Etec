#03) - Faça um algoritmo que receba um número e mostre uma mensagem caso este número 
# seja maior que 80, menor que 25 ou igual a 40. O usuário deverá informar se deseja continuar 
# informando os valores.

while True:
    
    nubero = int(input("Informe um número: "))

    if nubero > 80:
        print("O número é maior que 80")
    if nubero < 25:
        print("Numero menor que 25")
    if nubero == 40:
        print("Numero igual a 40")
        
    resposta = input("Deseja continuar (S/N)")
    
    if resposta.upper() == "N":
        break
2