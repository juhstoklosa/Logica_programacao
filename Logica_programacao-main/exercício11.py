materiais = ['Caneta','Calculadora','Grampeador','Canetão']
print(materiais)

print("---------------------------------------------------------------------")
                                  
materiais.append('Cadeira')       
materiais.append('Tela')          
print(materiais)                  
                                  
print("---------------------------------------------------------------------")

materiais.remove('Grampeador')
print(materiais)

print("========== ALMOXARIFADO ==========")
print(f"Os {len(materiais)} itens são:")

for i in materiais:
    print(f" -> {i}")

