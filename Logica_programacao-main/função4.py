def etiqueta(nome,categoria,preco):
    print("——————————————— Etiqueta ———————————————")
    print(f"• Nome: {nome}")
    print(f"• Categoria: {categoria}")
    print(f"• preço:     R${preco}")
    print("—————————————————————————————————————————")

produto = {
    "nome":  "     Funko Pop Naruto",
    "preco": 79.90,
    "categoria": "Colecionáveis"
}

etiqueta(produto["nome"], produto["categoria"], produto["preco"])