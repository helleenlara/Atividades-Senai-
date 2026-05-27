#Leia a idade de uma pessoa e classifique:
# Criança: até 12 anos 
# Adolescente: 13 a 17 
# Adulto: 18 a 59 
# Idoso: 60 ou mais 

idade = int(input("Qual a idade?: "))

if idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
else:
    print("Idoso")