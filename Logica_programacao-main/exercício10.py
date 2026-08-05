temperatura = [47,51,59,73,79,97]
soma = 0
for i in temperatura:
    if i <= 60:
        print("Normal!")
    elif i <= 80:
        print("Atenção!")
    else:
        print("Crítico!")
    

