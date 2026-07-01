produto = [
    ["Coca-Cola", "Refrigerante",12.50, 25],
    ["Bolacha",   "Comida",      3.50,  30],
    ["Alcatra",   "Carne",       39.90, 120],  
]

soma = 0
controle = 0
print("------------------Estoque-------------------")
for l in range(len(produto)):
    controle = (produto[l][2]*produto[l][3])
    print(f"Soma total produtos {l+1} é igual a {controle}")
    soma += (produto[l][2]*produto[l][3])

print(f"O valor Total do estoque é: R${soma}")