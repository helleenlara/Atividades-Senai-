#Crie um programa que peça uma senha ao usuário até que ele digite a senha correta.

senha_correta = "1234"
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta!")
    senha = input("Digite a senha novamente: ")

print("Acesso liberado!")