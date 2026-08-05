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

pedido = []
itens = []

def busca_produto(codigo):
    for linha in range(len(catalogo)):
        if catalogo[linha]['cod'] == codigo:
           nome_produto = catalogo[linha]['produto']

    return nome_produto 

def verifica_estoque(codigo,quant):
    for linha in range(len(catalogo)):
        if catalogo[linha]['cod'] == codigo:
            if quant <= catalogo[linha]['qtd_estoque']:
                print("Deseja continuar?")
            else:
                print("Erro ")

def calcula_total(codigo,quant):
    total = 0 
    for linha in range(len(catalogo)):
        if catalogo[linha]['cod'] == codigo:
           total = quant * catalogo[linha]['valor']
    return total 

continua = False
while  continua == False:
    codigo = int(input("Digite o codigo do Produto: "))
    quant = int(input("Digitr a quantidade desejada: "))

    nome_produto = busca_produto(codigo)
    ver_estoque = verifica_estoque(codigo,quant)
    valor_total = calcula_total(codigo,quant)

    print(f"Prod: {nome_produto} | Qtd : {quant} | Valor Tot: {valor_total}")

    desconto = "" 
    desconto = input("Deseja aplicar desconto S/N: ")
    if desconto  == "S":
        desconto = int(input("Valor desconto %:"))
        total_des = valor_total - ((valor_total*desconto)/100)
    pergunta_continua = input("Pretende continuar? S/N: ")
    iten = {
        "Nome:": nome_produto,
        "Quantidade:": quant,
        "Valor_Tot:": valor_total,
        "Valor_desc:": total_des
    }
    pedido.append(itens)
    if pergunta_continua == "N":
        continua = True
 
print(pedido)

print("——————————————————— Relátorio ——————————————————————") 
for lin in pedido:
    print(f"Produto: {lin["Nome"]:<13} Qtd: {lin["quantidade"]:<13}")
    print(f"valor Tot: {lin["Valor_tot"]:<13} | Total de desconto: {lin["Valor_desc"]} | Total final: {total_des}")
print("——————————————————————————————————————")
print("——————————————————— Fim do Relátorio ———————————————————")
