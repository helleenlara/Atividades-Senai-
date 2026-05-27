# Média de Vários Números

soma = 0
quantidade = 0

numero = int(input("Digite um número (0 para encerrar): "))

while numero != 0:
    soma += numero
    quantidade += 1
    numero = int(input("Digite outro número (0 para encerrar): "))

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print("Quantidade de números digitados:", quantidade)
print("Soma:", soma)
print("Média:", media)

