for i in range(1, 10, 1):
    
    n = float(input(f"Digite um numero o {i}° = "))
    if n > 0:
        print(f"Positivo")
    elif n < 0:
        print("Negativo")
    else:
        print("Zero")