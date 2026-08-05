continuar = True

while continuar:
    nome = input("Cadastre Aluno:")
    print(f"Aluno {nome} cadastrado!")

    resposta = input("Cadastrar novo? (s/n):")
    if resposta == "n":
        continuar = False

print("Cadastro finalizado!")