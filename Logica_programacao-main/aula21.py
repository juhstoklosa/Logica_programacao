produto = [
    ["Coca-Cola", "Refrigerante",12.50, 25],
    ["Bolacha",   "Comida",      3.50,  30],
    ["Alcatra",   "Carne",       39.90, 120],  
]

Total = 0
for l in range(len(produto)):
    print(f"Valor do produto: {produto[l][2]}")
    Total += produto[l][2] 
    
print(f"O valor total dos produtos é:{Total}")

