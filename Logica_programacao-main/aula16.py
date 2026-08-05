#i = 0
#for i in range(1,11):
    #if i % 2 == 0:
        #print(f"{i} é par")
    #else:
        #print(f"{i} é impar")


#notas = [8,7,0,5,2]

#print(notas[2])


#carros = ['Gol', 'Onix','Ka', 'Jetta']

#if carros [0] == 'Gol':
   # print("VW")
#elif carros [1] == "Ka":
    #print("Ford")

#print(carros[0])


#alunos = ["Aluno1", "Aluno2","Aluno3","Aluno4"]
#Primeira forma
#for i in range(len(alunos)):
    #print(alunos[i])

#Segunda forma
#for i in alunos:
    #print(i)


notas = [8.5,7.9,9.5,7,9,10]
soma = 0

for i in notas:
    soma += i

media = soma/len(notas)
print(f"Soma = {soma}")
print(f"Media = {media}")