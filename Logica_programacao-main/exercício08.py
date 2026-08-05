soma = 0
for chamados in range (1,6):
    total = float(input("Digite o tempo gasto:"))
    soma += total

print(f"a soma total foi:{soma}")
print(f"A média foi: {soma/chamados}")

