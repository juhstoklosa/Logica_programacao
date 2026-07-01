produto = {
    "nome":     "Action Figure Goku Ultra Instinct",
    "preco":    189.90,
    "estoque":  8,
    "desconto": 15
}

conta = produto["preco"]*produto["desconto"]/100
total = produto["preco"]-conta
final = total*produto["estoque"]

print("————————————— FICHA DO PRODUTO —————————————")

print(f"• Nome            : {produto["nome"]}")
print(f"• Preço           : R${produto["preco"]}")
print(f"• Desconto        : {produto["desconto"]}%")
print(f"• Preço final     : R${round(total,2)}")
print(f"• Estoque         : {produto["estoque"]}")
print(f"• Total em estoque: R${round(final,2)}")

print("————————————————————————————————————————————")

if produto["estoque"] > 0:
    print("→ Disponível!")
else: 
    print("→ Indisponível!")

print("————————————————————————————————————————————")
