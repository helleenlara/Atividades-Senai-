# Leia dois números e mostre qual deles é o maior. Caso sejam iguais, informe isso.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print(f"O numero {n1} é o maior")
elif n2 > n1:
    print(f"O numero {n2} é o maior")
else:
    print("Os numeros são iguais")
