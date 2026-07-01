Jogadores = ['Emilly','Esther','Julia', 'Ana']
pontuacoes = [3370, 4005, 3845, 4154]

print("---------------Placar da Partida-------------")
n = 0
maior = 0
destaque = 0

for i in Jogadores:
    print(f"{i} -> {pontuacoes[n]}")
    if maior < pontuacoes[n]:
        maior = pontuacoes[n]
        destaque = i
    n += 1

print("----------------------------------------------")

print(f"Maior pontuação: {maior}")
print(f"O destaque da partida foi: {destaque}✌️")





