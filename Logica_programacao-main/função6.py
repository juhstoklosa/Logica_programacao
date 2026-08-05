def total(preco, quan):
    tot = preco*quan
    return tot

print("———————————————————————————————————————————————")

resul = total(189.90,3)
print(f"• O total do pedido: R${resul}")

limite = 500

if resul > limite:
    print("→ AVISO: Este pedido requer aprovação do gerente!")
else: 
    print("→ Aprovado!")

print("———————————————————————————————————————————————")
