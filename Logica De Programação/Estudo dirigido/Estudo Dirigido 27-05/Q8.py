#Uma loja oferece:
# 10% de desconto para compras acima de R$100 
# 20% para compras acima de R$500 
# Leia o valor da compra e mostre o valor final.


valor = float(input("Digite o valor da compra: R$"))

if valor > 500:
    desconto = 0.20
elif valor > 100:
    desconto = 0.10
else:
    desconto = 0.0

valorf = valor - (valor * desconto)

print(f"Valor final da compra: R${valorf:.2f}")