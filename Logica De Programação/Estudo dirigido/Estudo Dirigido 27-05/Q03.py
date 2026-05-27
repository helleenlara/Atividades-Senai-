#Leia duas notas de um aluno, calcule a média e informe:
# Aprovado (média ≥ 7) 
# Recuperação (média entre 5 e 6.9) 
# Reprovado (média < 5) 

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1+nota2)/2

if media >= 7:
    print(f"Aprovado, sua media foi {media}")
elif media < 5:
    print(f"Reprovado, sua media foi {media}")
else:
    print(f"Sua media foi {media}, e você está na recuperação")
