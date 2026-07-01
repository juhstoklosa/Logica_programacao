

notas = [7, 3, 9, 2, 8, 5, 6, 1, 4, 10]
nomes = ["Ana","Bob","Cia","Dan","Eva",
"Ful","Gil","Hil","Ivo","Jao"]
aprovados = []
soma_aprovados = 0
conta_reprovados = 0
for i in range(len(notas)):
    if notas[i] >= 6:
        aprovados.append(nomes[i])
        soma_aprovados = soma_aprovados + notas[i] 
    else:
        conta_reprovados = conta_reprovados + 1
media = soma_aprovados / len(aprovados)
senha = soma_aprovados * 1000 + int(media) * 100 + conta_reprovados * 10 + len(nomes) * len(aprovados)
print("Senha:", senha)