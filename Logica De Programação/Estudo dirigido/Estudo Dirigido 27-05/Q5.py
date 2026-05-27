# Calculadora Simples

n1 = float(input("Digite o primeiro numero: "))
op = input("qual operação ( + ; x ; / ; - ): ")

while op not in ["+", "-", "x", "/"]:
    print("Operação invalida")
    op = input("qual operação ( + ; x ; / ; - ): ")

n2 = float(input("Digite o segundo numero: "))

if op == "+":
    re = n1 + n2
elif op == "-":
    re = n1 - n2
elif op == "x":
    re = n1 * n2
elif op == "/":
    while n2 == 0:
        print("Erro: não é possivel dividir por 0")
        n2 = float(input("Digite o segundo numero: "))
    re= n1/ n2

print("Total: ", re)