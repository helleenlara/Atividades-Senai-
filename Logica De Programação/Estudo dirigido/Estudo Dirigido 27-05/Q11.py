#Leia 5 números e mostre a soma total.

soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

print("A soma total é:", soma)