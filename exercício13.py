lista_pecas = []

while len(lista_pecas) < 6:
    peca= float(input(f"peça {len(lista_pecas)+1}: "))
    lista_pecas.append(peca)

print(f"As lista_pecas são: {lista_pecas}")

aprov = 0
reprov= 0 

print('----------------RELATÓRIO-----------------')
for contador in lista_pecas:
    if contador >= 9.8 and contador <= 10.2:
        print(f"{contador} mm -> Aprovado!")
        aprov += 1
    else:
        print(f"{contador} mm -> Rejeitado!")
        reprov += 1
print(f"Total de peças aprovadas: {aprov}")
print(f"Total de peças reprovadas: {reprov}")

    
                   