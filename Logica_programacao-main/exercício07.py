total = float(input("O total da compra foi:R$"))
parcelas = int(input("Quantidade de parcelas:"))
contador = 1
pago = 0
devedor = 0
valor_parcelas = total/parcelas


print(valor_parcelas)

print("========= CRONOGRAMA DE PAGAMENTOS =========")

while contador <= parcelas: 
    pago = pago + valor_parcelas
    devedor = total - pago
    print(f"{contador} | R${valor_parcelas} | R${pago} | R${devedor}")
    contador = contador+1

