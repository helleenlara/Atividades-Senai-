# Crie um programa que:
# Defina um número secreto 
# Peça tentativas ao usuário até ele acertar 
# Informe se o número digitado é maior ou menor que o secreto

n = 586

tentativa = int(input("Digite um numero: "))

while tentativa != n:
    if tentativa > n:
        print(f"{tentativa} é maior que o número secreto")
    elif tentativa < n:
        print(f"{tentativa} é menor que o número secreto")
    
    tentativa = int(input("Tente novamente: "))

print("Você acertou esse é o numero correto", n)