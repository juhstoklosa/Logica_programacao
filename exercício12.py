notas = []

while len(notas) < 4:
    avaliacao= float(input(f"Nota{len(notas)+1} :"))
    notas.append(avaliacao)

print(f"Notas registradas: {notas} ")

print("---------------- Relatório -----------------")
media = 0
for contador in notas:
    media = media + float(contador)
    if contador >= 8:
        print(f"{contador} -> Aprovado!")
    else:
        print(f"{contador} -> Reprovado!")
print(f"A media é: {(media/len(notas))}")