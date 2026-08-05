def total(valor,desconto,quant):
    tot = valor*quant
    desc = tot - (tot*desconto/100)
    return desc

produto = "Computador"
valor = 1500
desconto = 20
quant = 5

Total = total(valor,desconto,quant)
print("—————————————————————————————————————————————————————————")
print(f"• Produto: {produto} | → Vendido: {quant} | → Desconto: R${Total}")
print("—————————————————————————————————————————————————————————")