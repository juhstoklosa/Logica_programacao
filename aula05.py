print("======= Calculadora de Compras =======")
produto = input("Produto: ")
preco = float(input("Valor: R$"))
quantidade = int(input("Quantidade de produtos: "))
desconto = float(input("Valor do desconto: R$"))

print("======= Cupom de Compra =======")

print(f"Produto: {produto}")
print(f"Quantidade: {quantidade} unidades")
print(f"Valor: R${preco}")
print(f"Subtotal: R${preco*quantidade}")
print(f"Desconto: R${desconto}")
print(f"Total a pagar: R${(preco*quantidade)-desconto}")

print("========================================")





