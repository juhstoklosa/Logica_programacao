Produto = {
    "Nome":      "SSD NVMe 1TB",
    "Preço":     389.90,
    "Garantia":  3,
    "Estoque":   True
} 
print(f"→ {Produto["Nome"]}:")
print(f"• Preço: R${Produto["Preço"]}")
if Produto["Estoque"] == True:
    print("• Sim, temos estoque")
else:
    print("• Não, não temos estoque")

print(f"• Tempo de garantia: {Produto["Garantia"]} anos")
