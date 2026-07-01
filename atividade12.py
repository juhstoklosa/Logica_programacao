produto = {
    "nome":         "Mangá Demon Slayer Vol. 1",
    "preco":        34.90,
    "estoque":      2,
    "preco_minimo": 29.90,
}

print("——————————— ANTES DA ATUALIZAÇÃO ———————————")
print(f"• Preço atual: R${produto['preco']}")
print(f"• Estoque atual: {produto['estoque']} unidades")

print("—————————————————————————————————————————————")

print("————————————— APÓS A ATUALIZAÇÃO ————————————")
produto["preco"] = 28.00
print(f"• Preço novo: R${produto['preco']}")
produto["estoque"] += 10
print(f"• Estoque novo: {produto['estoque']} unidades")

produto["alerta"] = False
if produto["preco"] < produto["preco_minimo"]:
   produto["alerta"] = True
   
print(f"• Alerta de preço: {produto['alerta']}")
print("—————————————————————————————————————————————")
if produto["alerta"] == True:
   print("• O preço está abaixo do permitido!")
