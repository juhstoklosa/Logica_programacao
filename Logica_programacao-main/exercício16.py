catalogo = [
    {"cod": 1,  "produto": "Caneca Star Wars",          "valor": 39.90, "qtd_estoque": 25},
    {"cod": 2,  "produto": "Camiseta Marvel",           "valor": 59.90, "qtd_estoque": 30},
    {"cod": 3 , "produto": "Funko Pop Batman",          "valor": 89.90, "qtd_estoque": 15},
    {"cod": 4,  "produto": "Mousepad Geek RGB",         "valor": 49.90, "qtd_estoque": 20},
    {"cod": 5,  "produto": "Action Figure Goku",        "valor": 129.90,"qtd_estoque": 10},
    {"cod": 6,  "produto": "Boné Senhor dos Anéis",     "valor": 44.90, "qtd_estoque": 18},
    {"cod": 7,  "produto": "Quebra-cabeça Harry Potter","valor": 69.90, "qtd_estoque": 12},
    {"cod": 8,  "produto": "Chaveiro Pokémon",          "valor": 19.90, "qtd_estoque": 40},
    {"cod": 9,  "produto": "Luminária Mario Bros",      "valor": 79.90, "qtd_estoque": 14},
    {"cod": 10, "produto": "Caderno Anime",             "valor": 24.90, "qtd_estoque": 35},
]

def procura(codigo):
    nome = ""
    for lin in catalogo:
        if lin["cod"] == codigo:
            nome = lin["produto"]
    return nome

def verifica(quant,cod_pro):
    for lin in catalogo:
        if lin["cod"] == cod_pro:
           if  quant <= lin["qtd_estoque"]:
               print("Estoque ok")
           else:
               print("Estoque não ok")

def calcula_total(codigo,quant):
    total = 0 
    for linha in range(len(catalogo)):
        if catalogo[linha]['cod'] == codigo:
           total = quant * catalogo[linha]['valor']
    return total 



cod_produto = int(input("• Digite o código do Produto: "))
nome_produto = procura(cod_produto)
print(f"→ {nome_produto}")
quantidade = int(input("Digite a quantidade desejada: "))
verifica(quantidade,cod_produto)

valor_total = calcula_total(cod_produto,quantidade)

print(f"Prod {nome_produto} : Qtd : {quantidade} Valor Tot: {valor_total}")


