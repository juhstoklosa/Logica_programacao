produto = [
    {"Nome": "Computador", "marca": "Sonic PC", "estoque": 5,  "valor":2555.50},
    {"Nome": "Mouse     ",      "marca": "DexPC",    "estoque": 10, "valor":70.50},
    {"Nome": "Monitor   ",    "marca": "Dell",     "estoque": 15, "valor":650.50}
]

for i in range(len(produto)):
    print(f"• O produto → {produto[i]["Nome"]} | custa → R${produto[i]["valor"]}")