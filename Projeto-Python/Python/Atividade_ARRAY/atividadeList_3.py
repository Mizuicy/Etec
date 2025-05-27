num = []

for x in range(6):
    nums = int(input(f"Digite o {x + 1} = "))
    num.append(nums)

for x, num in enumerate(num):
    if num  % 2 == 0:
        print(f"{x}° par")
        par = x + x
        print(f"Resultado: {par}")
    else:
        print(f"{x}° impar")
        impar = x + x
        print(f"Resultado: {impar}")
    
