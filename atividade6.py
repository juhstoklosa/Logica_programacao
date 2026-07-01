loja = [
    ["TV 55",      "Samsung",     4800.00,  "Eletrônicos"],
    ["Geladeira",  "Brastemp",    3200.00,  "Eletrodomésticos"],
    ["Micro-ondas","Electrolux",  950.00,   "Eletrodomésticos"],
    ["Tablet",     "LG",          1800.00,  "Eletrônicos"],
]

controle = 0
soma = 0
print("-----------------Estoque----------------")
for lin in range(len(loja)):
    if (loja[lin][2]) >= 1000.00:
        print(f"Produto e Preço -> {loja[lin][0]} R${loja[lin][2]}")
        soma += (loja[lin][2]) 

print("-----------------------------------------")
print(f"O valor total de produtos é: R${soma}")
