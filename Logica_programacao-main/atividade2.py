dias = [ 'Segunda','Terça','Quarta', 'Quinta','Sexta',
         'Sabádo','Domingo']
treinos = [24, 30, 79, 43, 90, 82, 31]

print("----------Relatório de Treinos----------")
n = 0
total = 0
for i in dias:
    print(f"{i} -> {treinos[n]} min")
    total += treinos[n]
    n += 1 
print("-----------------------------------------")
print(f"Total {total} com media de {(total/len(dias))}")