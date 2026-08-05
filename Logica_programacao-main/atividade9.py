print("------------------------Pedidos----------------------------")
pedidos = [
    ["Pizza       ",        "Lanche   ",    45.90],
    ["Acai        ",         "Sobremesa", 32.00],
    ["X-Burguer   ",    "Lanche   ",    28.50],
    ["Frango Frito", "Prato    ",     38.90]
]

total = 0
for lin in range(len(pedidos)):
    print(f"• Produto:{pedidos[lin][0]} |• Categoria:{pedidos[lin][1]} |• Preço:R${pedidos[lin][2]}")
    if pedidos[lin][1] == "Lanche   ":
        total += pedidos[lin][2]

print("-----------------------------------------------------------")
print(f"→ O preço total foi: R${total}")
