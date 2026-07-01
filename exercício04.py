item = input("Nome do item:")
atual = int(input("Quantidade atual:"))
maximo = int(input("Quantidade máxima:"))

minimo = (maximo*20)/100

if atual <= minimo:
    print("REPOR URGENTE")
elif atual >= maximo:
    print("Adequado")

print("======= Relatório de Estoque =======")

print(f"Item {item}")
print(f"Quantidade atual: {atual}")
print(f"Quantidade máxima: {maximo}")
print(f"Limite mínimo: {minimo}")


