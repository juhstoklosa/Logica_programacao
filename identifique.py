telefone = input("Informe o telefone: ")
 
telefone_limpo = telefone.replace("(", "")
telefone.replace(")", "")
telefone.replace("-", "")
telefone.replace(" ", "")
 
print(f"Telefone original: {telefone}")
print(f"Telefone limpo: {telefone_limpo}")
print(f"Quantidade de dígitos: {len(telefone_limpo)}")
