print("—————————————————————————————————————————")

def calcular_total(prec, quantidade):
    total = preco * quantidade
    print(f"Total: R${total}")
    return total

def aplicar_desconto(total,percentual):
    tot_final = total -(total *percentual/100)
    print(f"Valor final: R${tot_final}")
    return tot_final

def processar_pedido(cliente,prod,prec,quant,perc):
    cliente = (nome)
    print(f"Nome: {cliente}")
    prod = (produto)
    print(f"Produto: {prod}")
    prec = (preco)
    print(f"Preço: R${prec}")
    quant = (quantidade)
    print(f"Quantidade: {quant} unidades")
    perc = (percentual)
    print(f"Percentual: {perc}%")


nome = input("Digite seu nome: ")
produto = input("Digite o nome do produto: ")
print("————————————————————————————")
preco = int(input("Digite o preço: R$"))
quantidade = int(input("Digite a quantidade desejada: "))
percentual = int(input("Digite o desconto: "))

total = calcular_total(preco,quantidade)
tot_final = aplicar_desconto(total, percentual)
print("————————————————————————————")
processar_pedido(nome,produto,preco,quantidade,percentual)
print("————————————————————————————")


