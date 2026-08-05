selecoes = [
    {"nome": "Brasil  ",   "gols_pro": 12, "gols_contra": 4, "vitorias": 4},
    {"nome": "França  ",   "gols_pro":  9,  "gols_contra": 5, "vitorias": 3},
    {"nome": "Marrocos", "gols_pro":   6,  "gols_contra": 7, "vitorias": 2},
    {"nome": "Croácia ",  "gols_pro":  8,  "gols_contra": 6, "vitorias": 3},
]

saldo = 0
print("————————————————————————————————————————————————————————————————————————————————————————") 
for lin in selecoes:
    classificado = ""
    saldo = ((lin["gols_pro"])-(lin["gols_contra"]))
    if lin["vitorias"] > 3:
        classificado = "• CLASSIFICADO!"
    else:
        classificado = "• NÃO CLASSIFICADO!"
    print(f"• {lin["nome"]:<4} | → Pró {lin['gols_pro']:<4} | → contra {lin["gols_contra"]:<4} |"
          f" → Saldo {saldo:<4} | → Vitórias {lin["vitorias"]:<4} | {classificado:<4}")
print("————————————————————————————————————————————————————————————————————————————————————————") 

    

