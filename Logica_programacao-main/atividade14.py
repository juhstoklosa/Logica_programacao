selecao = {
    "nome":     " Brasil",
    "jogos":    7,
    "gols":     17,
    "vitorias": 6,
    "grupo":    "C"
}

print("————————————— FICHA DE SELEÇÃO —————————————") 
for lin in selecao:
    print(f"• {lin}: {selecao[lin]}") 
    if lin == "vitorias":
        if selecao[lin] > 5:
            print("→ Ótima Campanha!")

print("————————————————————————————————————————————")
media = selecao["gols"]/selecao["jogos"]
print(f"→ Média de gols: {round(media,2)}")
tot = (selecao["vitorias"]/selecao["jogos"])*100
print(f"→ Aproveitamento: {round(tot,2)}%")
print("————————————————————————————————————————————") 





        