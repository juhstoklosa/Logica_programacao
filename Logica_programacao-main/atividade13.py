produto = {
    "nome":     "Controle PS5 DualSense",
    "preco":    499.90,
    "estoque": 5,
    "parcelas": 10
}

print("————————————— RELATÓRIO TÉCNICO —————————————")    
for linha in produto:
    if type(produto[linha]) == str:
        print(f"• {linha}: {produto[linha]}")
    if type(produto[linha]) == float:
        print(f"• {linha}: R${produto[linha]}")
    if type(produto[linha]) == int:
        print(f"• {linha}: R${produto[linha]}")

print("————————————————————————————————————————————")
print("————————————————————————————————————————————")

estoque = produto["preco"]*produto["estoque"]
print(f"→ Total em estoque: R${estoque}")
parcelas = produto["preco"]/produto["parcelas"]
print(f"→ Valor das parcelas: R${round(parcelas,2)}")
print("————————————————————————————————————————————")