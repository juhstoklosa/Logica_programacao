def soma(A,B):
    soma = A + B
    return soma

def sub(A,B):
    sub = A - B
    return sub

def verifica(A,B):
    validador = False
    if A != B :
        validador = True
    return validador

dado1 = input("Digite palavra 1: ")
dado2 = input("Digite palavra 2: ")

verifica(dado1,dado2)

confere = verifica(dado1,dado2)

if confere == True:
    print("Diferente")
else:
    print("Igual")