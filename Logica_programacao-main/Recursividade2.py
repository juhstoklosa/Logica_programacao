def tabuada(n):
    if n == 0:
        print("Fim!")
        return 
    #Calculo Básico!
    camada = "Camada "+str(n)
    total = 5*n
    resultado = "→ 5*"+str(n)+"= "+str(total)
#—————————————————————————————————————————
    tabuada(n-1) #Recursiva
    print(camada)
    print(resultado)

tabuada(5)